from flask_wtf import form
# these are the form types that we want
from wtforms import StringField, PasswordField
# this is what we use to validate and make set qualifications
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, Length, EqualTo

from models import User


def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User with that name already exists.')


def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email already exists.')


class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(),
                                                   Regexp(r'^[a-zA-Z0-9_]+$', message=("Username should be one word, letters, numbers and underscores only.")), name_exists])
    email = StringField('Email', validators=[
                        DataRequired(), Email(), email_exists])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=7), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm Password', validators=[
        DataRequired())])
