"""
Module for messages form.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, validators


class MessageForm(FlaskForm):
    """
    Class contains format of  form message field.
    """
    message = StringField("message", [validators.Length(max=100)])
