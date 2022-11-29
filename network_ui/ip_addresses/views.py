import re, subprocess
from network_ui import db
from network_ui.ip_addresses.models import IPAddress
from network_ui.ip_addresses.forms import AddForm, DeleteForm
from network_ui.nw_handicaps.models import NetworkHandicap
from flask import Blueprint, render_template, url_for, redirect, flash

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
        flash("a script is running please wait before adding a new one")
        return redirect(url_for("index"))

    if form.validate_on_submit():

        pc_name = form.pc_name.data
        ip_address = form.ip_address.data
        network_handicap = form.network_handicap.data

        # validate the ip addess with re
        # https://www.geeksforgeeks.org/python-program-to-validate-an-ip-address/
        regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        if re.search(regex, ip_address):

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

            new_ip_address = IPAddress(pc_name, ip_address, network_handicap)
            db.session.add(new_ip_address)
            db.session.commit()

            return redirect(url_for("index"))
        else:
            # TODO: send a flash to the user and dont save the IP
            flash(f"{ip_address} is not a valid IP address")

    # if the network handicap is empty, ask the user to add one first before adding an ip
    if NetworkHandicap.query.all() == []:
        flash("Add a Network Profile first to add an ip address")
        return redirect(url_for("nw_handi.add"))

    return render_template("add_ip_address.html", form=form)


@ip_address_blueprint.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    ip_address = IPAddress.query.get(id)
    if ip_address:
        db.session.delete(ip_address)
        db.session.commit()

    return redirect(url_for("index"))
