from network_ui import db
from network_ui.nw_handicaps.forms import AddForm
from network_ui.nw_handicaps.models import NetworkHandicap
from flask import Blueprint, render_template, url_for, redirect, flash, request
from markupsafe import Markup


nw_handicap_blueprint = Blueprint(
    "nw_handi", __name__, template_folder="templates/nw_handicaps/"
)


@nw_handicap_blueprint.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        handicap_name = form.nw_handicap_name.data
        bandwidth_restriction_upload = form.bandwidth_restriction_upload.data
        bandwidth_restriction_download = form.bandwidth_restriction_download.data

        dns_latency = form.dns_latency.data
        general_latency = form.general_latency.data

        packet_loss = form.packet_loss.data

        if form.cidr_not.data and form.cidr_suffix.data:
            cidr_notation = f"{form.cidr_not.data}/{form.cidr_suffix.data}"
            print(cidr_notation)
        elif form.cidr_not.data and not form.cidr_suffix.data:
            cidr_notation = None
            flash(
                Markup(f"Add the suffix {form.cidr_not.data} / <b>----</b>"), "warning"
            )

            return redirect(url_for("nw_handi.add"))
        else:
            cidr_notation = None
            flash(
                Markup(
                    f"the subnet mask you entered is wrong > '<b>{form.cidr_not.data}/{form.cidr_suffix.data}</b>'"
                ),
                "danger",
            )

            return redirect(url_for("nw_handi.add"))

        # check the Handicap name is already existing on DB
        if NetworkHandicap.query.filter_by(handicap_name=handicap_name).first() != None:
            flash(
                Markup(f"This handicap name <b>{handicap_name}</b> is already in use"),
                "danger",
            )
            return redirect(url_for("nw_handi.add"))

        new_nw_handicap = NetworkHandicap(
            handicap_name,
            bandwidth_restriction_upload,
            bandwidth_restriction_download,
            dns_latency,
            general_latency,
            packet_loss,
            cidr_notation,
        )

        db.session.add(new_nw_handicap)
        db.session.commit()

        return redirect(url_for("index"))
    if request.method == "POST":
        flash(
            "Enter value for at least one parameter to save the handicap template",
            "danger",
        )
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
    return redirect(url_for("nw_handi.list"))


@nw_handicap_blueprint.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = AddForm()

    handicap_to_update = NetworkHandicap.query.get_or_404(id)
    print(handicap_to_update)

    if form.validate_on_submit():

        updated_handicap_name = form.nw_handicap_name.data

        # check the Handicap name is already existing on DB
        if (
            NetworkHandicap.query.filter_by(handicap_name=updated_handicap_name).first()
            != None
            and handicap_to_update.handicap_name != updated_handicap_name
        ):
            flash(
                Markup(
                    f"This handicap name <b>{form.nw_handicap_name.data}</b> is already in use"
                ),
                "danger",
            )
            return redirect(url_for("nw_handi.list"))

        handicap_to_update.handicap_name = form.nw_handicap_name.data
        handicap_to_update.bandwidth_restriction_upload = (
            form.bandwidth_restriction_upload.data
        )
        handicap_to_update.bandwidth_restriction_download = (
            form.bandwidth_restriction_download.data
        )

        handicap_to_update.dns_latency = form.dns_latency.data
        handicap_to_update.general_latency = form.general_latency.data

        handicap_to_update.packet_loss = form.packet_loss.data
        # TODO: Add logic to limit the value between 0 - 100
        db.session.commit()
        flash(
            Markup(f"<b>{handicap_to_update.handicap_name}</b> updated successfully"),
            "success",
        )
        return redirect(url_for("nw_handi.list"))
    return render_template(
        "update_nw_handicap.html", form=form, handicap_to_update=handicap_to_update
    )
