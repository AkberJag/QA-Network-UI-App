import re
from network_ui import db
from network_ui.ip_addresses.models import IPAddress
from network_ui.ip_addresses.forms import AddForm, DeleteForm
from flask import Blueprint, render_template, url_for, redirect

ip_address_blueprint = Blueprint(
    "ipaddresses", __name__, template_folder="templates/ip_addresses/"
)


@ip_address_blueprint.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        pc_name = form.pc_name.data
        ip_address = form.ip_address.data

        # validate the ip addess with re
        # https://www.geeksforgeeks.org/python-program-to-validate-an-ip-address/
        regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        if re.search(regex, ip_address):
            new_ip_address = IPAddress(pc_name, IPAddress)
            db.session.add(new_ip_address)
            db.session.commit()
        else:
            print("Invalid Ip address")
            # TODO: send a flash to the user and dont save the IP
        return redirect(url_for("index"))
    return render_template("add_ip_address.html")


@ip_address_blueprint.route("/delete", methods=["GET", "POST"])
def delete():
    form = DeleteForm()

    if form.validate_on_submit():
        id = form.id.data

        ip_address = IPAddress.query.get(id)

        db.session.delete(ip_address)
        db.session.commit()

        return redirect(url_for("index"))
    return render_template("delete_ip_address.html", form=form)
