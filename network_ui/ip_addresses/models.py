from network_ui import db
from network_ui.nw_handicaps.models import NetworkHandicap


class IPAddress(db.Model):
    __tablename__ = "ipaddress"

    id = db.Column(db.Integer, primary_key=True)

    pc_name = db.Column(db.Text, unique=True)
    ip_address = db.Column(db.Text, unique=True)

    network_handicap = db.Column(db.Integer, db.ForeignKey("networkhandicaps.id"))

    def __init__(self, pc_name, ip_address, network_handicap):
        self.pc_name = pc_name
        self.ip_address = ip_address
        self.network_handicap = network_handicap

    def __repr__(self) -> str:
        return f"PC name: {self.pc_name} ({self.ip_address})'s profile is  {NetworkHandicap.query.get(self.network_handicap).handicap_name}"
