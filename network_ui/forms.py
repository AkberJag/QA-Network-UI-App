from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, FloatField, SubmitField


class AddIPForm(FlaskForm):
    pc_name = StringField("Name of the PC:")
    ip_address = StringField("Enter IP address:")

    submit = SubmitField("Add IP Address")


class DeleteIPForm(FlaskForm):
    id = IntegerField("Enter id of the IP Address:")
    submit = SubmitField("Delete IP Address")


class AddNetworkHandicapForm(FlaskForm):
    name = StringField("Enter handicap name: ")
    bandwidth_rest_upload = FloatField("Bandwidth restriction max upload: ")
    bandwidth_rest_download = FloatField("Bandwidth restriction max download: ")
    dns_latency = FloatField("DNS Latency: ")
    general_latency = FloatField("General Latency: ")
    packet_loss = FloatField("Packet Loss (0 to 100%): ")

    submit = SubmitField("Add network handicap type")


class DeleteNetworkHandicapForm(FlaskForm):
    id = IntegerField("Enter id of the handicap type:")
    submit = SubmitField("Delete handicap type")
