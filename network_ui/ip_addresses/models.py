from network_ui import db


class IPAddress(db.Model):
    __tablename__ = "ipaddress"

    id = db.Column(db.Integer, primary_key=True)

    pc_name = db.Column(db.Text)
    ip_address = db.Column(db.Text)
    network_handicap = db.relationship(
        "NetworkHandicap", backref="ipaddress", uselist=False
    )

    def __init__(self, pc_name, ip_address):
        self.pc_name = pc_name
        self.ip_address = ip_address
