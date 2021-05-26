from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class LoginForm(FlaskForm):
    user = StringField("Users", [validators.Length(max=100), validators.DataRequired()])
    password = PasswordField("Password", [validators.Length(max=100), validators.InputRequired()])


class RegisterForm(FlaskForm):
    first_name = StringField("First Name", [validators.Length(max=100), validators.DataRequired()])
    last_name = StringField("Last Name", [validators.Length(max=100), validators.DataRequired()])
    email = StringField("Email", [validators.Length(max=100), validators.DataRequired()])
