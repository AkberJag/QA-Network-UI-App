from network_ui import db


class NetworkHandicap(db.Model):
    """a template system with pre-configured named settings"""

    __tablename__ = "networkhandicaps"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text)
    bandwidth_rest_upload = db.Column(db.Float)
    bandwidth_rest_download = db.Column(db.Float)
    dns_latency = db.Column(db.Float)
    general_latency = db.Column(db.Float)
    packet_loss = db.Column(db.Float)

    def __init__(
        self,
        name,
        bandwidth_rest_upload,
        bandwidth_rest_download,
        dns_latency,
        general_latency,
        packet_loss,
    ):
        self.name = name
        self.bandwidth_rest_upload = bandwidth_rest_upload
        self.bandwidth_rest_download = bandwidth_rest_download
        self.dns_latency = dns_latency
        self.general_latency = general_latency
        self.packet_loss = packet_loss


class IPAddress(db.Model):
    __tablename__ = "ipaddresses"

    id = db.Column(db.Integer, primary_key=True)

    ip_address = db.Column(db.Text)
    pc_name = db.Column(db.Text)
    # In the future this is replaced with the current logged in user's name
    added_by = db.Column(db.Text)

    def __init__(self, ip_address, pc_name, added_by) -> None:
        self.ip_address = ip_address
        self.pc_name = pc_name
        self.added_by = added_by
