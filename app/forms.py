from flask_wtf import FlaskForm
from wtforms.fields import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField, PasswordField
)
from wtforms.validators import DataRequired, ValidationError


v = [DataRequired()]


class LoginForm(FlaskForm):
    employee_number = StringField("Employee number", v)
    password = PasswordField("Password", v)
    submit = SubmitField("Login")
