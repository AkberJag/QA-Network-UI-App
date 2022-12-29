import subprocess
from network_ui import db
from network_ui.ip_addresses.models import IPAddress
from network_ui.ip_addresses.forms import AddForm, DeleteForm
from network_ui.nw_handicaps.models import NetworkHandicap
from flask import Blueprint, render_template, url_for, redirect, flash
from markupsafe import Markup
from network_ui.helpers.helpers_common import validate_ip_address

ip_address_blueprint = Blueprint(
    "ipaddresses", __name__, template_folder="templates/ip_addresses/"
)


# this flag is to prevent multiple users from running script simultaniously
# Ask help for a better implementaion of this.
is_a_scrip_running = False


@ip_address_blueprint.route("/add", methods=["GET", "POST"])
def add():
    global is_a_scrip_running

    form = AddForm()
    form.network_handicap.choices = [
        (g.id, g.handicap_name) for g in NetworkHandicap.query.all()
    ]

    # if a script is running already take the user to the homescreen and show a flash
    if is_a_scrip_running:
        flash("a script is running please wait before adding a new one", "danger")
        return redirect(url_for("index"))

    if form.validate_on_submit():

        pc_name = form.pc_name.data
        ip_address = form.ip_address.data
        network_handicap = form.network_handicap.data

        # check the PC name is already existing on DB
        if IPAddress.query.filter_by(pc_name=pc_name).first() != None:
            flash(
                Markup(f"This PC name <b>{pc_name}</b> is already in use"),
                "danger",
            )
            return redirect(url_for("ipaddresses.add"))
        # check the IP Address is already existing on DB
        if IPAddress.query.filter_by(ip_address=ip_address).first() != None:
            flash(
                Markup(f"This IP address <b>{ip_address}</b> is already in use"),
                "danger",
            )
            return redirect(url_for("ipaddresses.add"))

        if validate_ip_address(ip_address):

            # run the script with subprocess and if it is succesful, add the details to DB
            is_a_scrip_running = True

            # commenting to test this on windows
            # script_call = subprocess.call(
            #     [
            #         "bash",
            #         "network_ui/shell_scripts/temp.sh",
            #         str(ip_address),
            #         str(network_handicap),
            #     ]
            # )

            script_call = 0

            if str(script_call) == "0":
                is_a_scrip_running = False

            # Increment the total number PCs configured in this template by 1
            # Please see the question on nw_handicaps > models.py
            NetworkHandicap.query.get(int(network_handicap)).no_of_pcs = (
                NetworkHandicap.query.get(int(network_handicap)).no_of_pcs + 1
            )

            new_ip_address = IPAddress(pc_name, ip_address, network_handicap)
            db.session.add(new_ip_address)
            db.session.commit()

            flash(Markup(f"IP address added successfully"), "success")
            return redirect(url_for("index"))
        else:
            flash(Markup(f"{ip_address} is not a valid IP address"), "danger")

    # if the network handicap is empty, ask the user to add one first before adding an ip
    if NetworkHandicap.query.all() == []:
        flash("Add a Network Profile first to add an ip address", "warning")
        return redirect(url_for("nw_handi.add"))

    return render_template("add_ip_address.html", form=form)


@ip_address_blueprint.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    ip_address = IPAddress.query.get(id)
    if ip_address:

        # Decrement the total number PCs configured in this template by 1
        # Please see the question on nw_handicaps > models.py
        NetworkHandicap.query.get(int(ip_address.network_handicap)).no_of_pcs = (
            NetworkHandicap.query.get(int(ip_address.network_handicap)).no_of_pcs - 1
        )

        db.session.delete(ip_address)
        db.session.commit()

        # TODO: Add a script call to remove this IP address from the restriction

    return redirect(url_for("index"))
