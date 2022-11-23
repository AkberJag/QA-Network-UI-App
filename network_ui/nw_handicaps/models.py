from network_ui import db


class NetworkHandicap(db.Model):
    __tablename__ = "networkhandicaps"

    id = db.Column(db.Integer, primary_key=True)

    handicap_name = db.Column(db.Text)  # Eg: good network

    ip_address_id = db.Column(db.Integer, db.ForeignKey("ipaddress.id"))

    def __init__(self, handicap_name, ip_address_id):
        self.handicap_name = handicap_name
        self.ip_address_id = ip_address_id
