from network_ui import db


class NetworkHandicap(db.Model):
    __tablename__ = "networkhandicaps"

    id = db.Column(db.Integer, primary_key=True)

    handicap_name = db.Column(db.Text, unique=True)  # Eg: good network

    bandwidth_restriction_upload = db.Column(db.Float)
    bandwidth_restriction_download = db.Column(db.Float)

    dns_latency = db.Column(db.Float)
    general_latency = db.Column(db.Float)
    packet_loss = db.Column(db.Float)

    # this is to hold the total number of pcs configured for a template
    # ? Question: is this a better way or joining 2 tables and counting is better?
    no_of_pcs = db.Column(db.Integer, default=0)

    # https://docs.sqlalchemy.org/en/14/orm/cascades.html
    # cascade will auto delete the child when the parent is deleted
    ip_address_id = db.relationship(
        "IPAddress",
        backref="networkhandicaps",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )

    def __init__(
        self,
        handicap_name,
        bandwidth_restriction_upload,
        bandwidth_restriction_download,
        dns_latency,
        general_latency,
        packet_loss,
    ):
        self.handicap_name = handicap_name
        self.bandwidth_restriction_upload = bandwidth_restriction_upload
        self.bandwidth_restriction_download = bandwidth_restriction_download
        self.dns_latency = dns_latency
        self.general_latency = general_latency
        self.packet_loss = packet_loss
