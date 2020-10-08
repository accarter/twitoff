from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    user_id = IntegerField("User ID:")
    text = StringField("Tweet: ")
    submit = SubmitField("Add Tweet")
