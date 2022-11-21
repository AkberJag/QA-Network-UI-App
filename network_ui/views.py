from network_ui import db
from network_ui import app
from network_ui.forms import (
    AddIPForm,
    AddNetworkHandicapForm,
    DeleteIPForm,
    DeleteNetworkHandicapForm,
)
from network_ui.models import IPAddress, NetworkHandicap
from flask import render_template, url_for, redirect


@app.route("/addnwh", methods=["GET", "POST"])
def add_template():
    form = AddNetworkHandicapForm()

    if form.validate_on_submit():
        name = form.name.data
        bandwidth_rest_upload = form.bandwidth_rest_upload.data
        bandwidth_rest_download = form.bandwidth_rest_download.data
        dns_latency = form.dns_latency.data
        general_latency = form.general_latency.data
        packet_loss = form.packet_loss.data

        return redirect(url_for("restrictions"))
    return render_template("add_nwh.html", form=form)


@app.route("/list", methods=["GET", "POST"])
def restrictions():
    ipaddesses = IPAddress.query.all()
    return render_template("list_restrictions.html", ipaddesses=ipaddesses)
