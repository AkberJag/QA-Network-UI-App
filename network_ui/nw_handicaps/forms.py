from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField
from wtforms.validators import InputRequired


class AddForm(FlaskForm):
    nw_handicap_name = StringField(
        "Name of handicap template:", validators=[InputRequired()]
    )
    bandwidth_restriction_upload = FloatField(
        "Enter Bandwidth restriction - max upload:"
    )
    bandwidth_restriction_download = FloatField(
        "Enter Bandwidth restriction - max download:"
    )
    dns_latency = FloatField("DNS Latency (In seconds):")
    general_latency = FloatField("General Latency (In seconds):")

    packet_loss = FloatField("Packet Loss %:")

    submit = SubmitField("Add handicap template")
