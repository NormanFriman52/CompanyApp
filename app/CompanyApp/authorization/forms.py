"""
Module for Login and Register form.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class LoginForm(FlaskForm):
    """
    Class contains format of form user and password fields.
    """
    user = StringField("Users", [validators.Length(max=100), validators.DataRequired()])
    password = PasswordField("Password", [validators.Length(max=100), validators.InputRequired()])


class RegisterForm(FlaskForm):
    """
    Class contains format of form first_name, email and last_name fields.
    """
    first_name = StringField("First Name", [validators.Length(max=100), validators.DataRequired()])
    last_name = StringField("Last Name", [validators.Length(max=100), validators.DataRequired()])
    email = StringField("Email", [validators.Length(max=100), validators.DataRequired()])
