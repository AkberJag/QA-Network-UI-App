from network_ui import app
from flask import render_template
from network_ui.ip_addresses.models import IPAddress


@app.route("/")
def index():
    ip_addresses = IPAddress.query.all()
    return render_template("home.html", ip_addresses=ip_addresses)


if __name__ == "__main__":
    app.run(debug=True)
