# file to define website forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from myproject.models import User
from myproject import bcrypt


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    login_button = SubmitField("Sign in")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError("E-mail not found. Create an account to continue.")


class FormCreateAccount(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(6, 20)])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), EqualTo("password")])
    submit_button = SubmitField("Create account")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("E-mail already registered. Sign up with a different e-mail or Sign in to continue.")


class FormPhoto(FlaskForm):
    photo = FileField("Photo", validators=[DataRequired()])
    upload_button = SubmitField("Upload photo")
