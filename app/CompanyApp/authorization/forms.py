from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class LoginForm(FlaskForm):
    user = StringField("Users", [validators.Length(max=100), validators.DataRequired()])
    password = PasswordField("Password", [validators.Length(max=100), validators.InputRequired()])
