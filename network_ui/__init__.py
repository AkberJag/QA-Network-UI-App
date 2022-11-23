import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__name__))

app = Flask(__name__)

app.config["SECRET_KEY"] = "ThisIsASecretKey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

Migrate(app, db)


from network_ui.ip_addresses.views import ip_address_blueprint
from network_ui.nw_handicaps.views import nw_handicap_blueprint

app.register_blueprint(ip_address_blueprint, url_prefix="/ipaddr")
app.register_blueprint(nw_handicap_blueprint, url_prefix="/nwh")
