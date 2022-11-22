from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField


class AddForm(FlaskForm):
    pc_name = StringField("Enter PC name: ")
    ip_address = StringField("Enter IP Address: ")

    submit = SubmitField("Add IP Address")


class DeleteForm(FlaskForm):
    id = IntegerField("Enter id of the IP address: ")
    submit = SubmitField("Delete IP Address")
