from network_ui import db


class NetworkHandicap(db.Model):
    __tablename__ = "networkhandicaps"

    id = db.Column(db.Integer, primary_key=True)

    handicap_name = db.Column(db.Text)  # Eg: good network

    bandwidth_restriction_upload = db.Column(db.Float)
    bandwidth_restriction_download = db.Column(db.Float)

    dns_latency = db.Column(db.Float)
    general_latency = db.Column(db.Float)
    packet_loss = db.Column(db.Float)

    ip_address_id = db.relationship(
        "IPAddress", backref="networkhandicaps", uselist=False
    )

    def __init__(
        self,
        handicap_name,
        ip_address_id,
        bandwidth_restriction_upload,
        bandwidth_restriction_download,
        dns_latency,
        general_latency,
        packet_loss,
    ):
        self.handicap_name = handicap_name
        self.ip_address_id = ip_address_id
        self.bandwidth_restriction_upload = bandwidth_restriction_upload
        self.bandwidth_restriction_download = bandwidth_restriction_download
        self.dns_latency = dns_latency
        self.general_latency = general_latency
        self.packet_loss = packet_loss
