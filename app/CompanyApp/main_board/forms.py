from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class MessageForm(FlaskForm):
    message = StringField("message", [validators.Length(max=100)])
