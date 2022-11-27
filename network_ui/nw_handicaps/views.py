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

        new_nw_handicap = NetworkHandicap(handicap_name, ip_address_id)

        db.session.add(new_nw_handicap)
        db.session.commit()

        return redirect(url_for("index"))
    return render_template("add_nw_handicap.html", form=form)
