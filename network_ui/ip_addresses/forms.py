from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, SelectField


class AddForm(FlaskForm):
    # TODO: Make this field unique
    pc_name = StringField("Enter PC name: ")

    # TODO: Make this field unique
    ip_address = StringField("Enter IP Address: ")
    network_handicap = SelectField("Selecet Network Profile:")

    submit = SubmitField("Add IP Address")


class DeleteForm(FlaskForm):
    id = IntegerField("Enter id of the IP address: ")
    submit = SubmitField("Delete IP Address")
