from network_ui import db
from network_ui.nw_handicaps.forms import AddForm
from network_ui.nw_handicaps.models import NetworkHandicap
from flask import Blueprint, render_template, url_for, redirect


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

        new_nw_handicap = NetworkHandicap(
            handicap_name,
            ip_address_id,
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
