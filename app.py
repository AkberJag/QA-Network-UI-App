from network_ui import app, db
from flask import render_template
from network_ui.ip_addresses.models import IPAddress
from network_ui.nw_handicaps.models import NetworkHandicap


@app.route("/")
def index():
    ip_addresses = IPAddress.query.all()
    all_templates = NetworkHandicap.query.all()

    templates = {}
    for template in all_templates:
        templates[template.id] = {
            "pc": (
                db.session.query(IPAddress, NetworkHandicap)
                .select_from(IPAddress)
                .join(NetworkHandicap)
                .filter(IPAddress.network_handicap == template.id)
                .all()
            ),
            "template": template,
        }
    return render_template("home.html", templates=templates)


if __name__ == "__main__":
    app.run(debug=True)
