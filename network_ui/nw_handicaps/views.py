from network_ui import db
from network_ui.nw_handicaps.forms import AddForm
from network_ui.nw_handicaps.models import NetworkHandicap
from flask import Blueprint, render_template, url_for, redirect, flash
from markupsafe import Markup


nw_handicap_blueprint = Blueprint(
    "nw_handi", __name__, template_folder="templates/nw_handicaps/"
)


@nw_handicap_blueprint.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        handicap_name = form.nw_handicap_name.data
        ip_address_id = form.ip_address_id.data
        bandwidth_restriction_upload = form.bandwidth_restriction_upload.data
        bandwidth_restriction_download = form.bandwidth_restriction_download.data

        dns_latency = form.dns_latency.data
        general_latency = form.general_latency.data

        packet_loss = form.packet_loss.data
        # TODO: Add logic to limit the value between 0 - 100

        # check the Handicap name is already existing on DB
        if NetworkHandicap.query.filter_by(handicap_name=handicap_name).first() != None:
            flash(Markup(f"This Markup name <b>{handicap_name}</b> is already in use"))
            return redirect(url_for("nw_handi.add"))

        new_nw_handicap = NetworkHandicap(
            handicap_name,
            bandwidth_restriction_upload,
            bandwidth_restriction_download,
            dns_latency,
            general_latency,
            packet_loss,
        )

        db.session.add(new_nw_handicap)
        db.session.commit()

        return redirect(url_for("index"))
    return render_template("add_nw_handicap.html", form=form)


@nw_handicap_blueprint.route("/list", methods=["GET", "POST"])
def list():
    nw_handicaps = NetworkHandicap.query.all()

    return render_template("list_all_handicaps.html", nw_handicaps=nw_handicaps)


@nw_handicap_blueprint.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    ip_address = NetworkHandicap.query.get(id)
    if ip_address:
        db.session.delete(ip_address)
        db.session.commit()

        # TODO: Add a script call to remove this IP address from the restriction
        # TODO: along with the template deletion, delete all the IP address configured with the template
    return redirect(url_for("index"))
