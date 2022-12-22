from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField
from wtforms.validators import InputRequired, Optional


class AddForm(FlaskForm):
    nw_handicap_name = StringField(
        "Name of handicap template:", validators=[InputRequired()]
    )
    bandwidth_restriction_upload = FloatField(
        "Enter Bandwidth restriction - max upload:", validators=[Optional()]
    )
    bandwidth_restriction_download = FloatField(
        "Enter Bandwidth restriction - max download:", validators=[Optional()]
    )
    dns_latency = FloatField("DNS Latency (In seconds):", validators=[Optional()])
    general_latency = FloatField(
        "General Latency (In seconds):", validators=[Optional()]
    )

    packet_loss = FloatField("Packet Loss %:", validators=[InputRequired()])

    submit = SubmitField("Add handicap template")
