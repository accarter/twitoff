from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    username = StringField("Username: ")
    followers = IntegerField("Number of followers: ")
    submit = SubmitField("Add User")
