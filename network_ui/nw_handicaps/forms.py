from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField


class AddForm(FlaskForm):
    nw_handicap_name = StringField("Name of handicap template:")
    ip_address_id = IntegerField("Enter id of the ip address:")
    submit = SubmitField("Add handicap template")
