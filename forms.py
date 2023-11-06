from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Length(min=3, max=255)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=64)])


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Length(min=3, max=255)])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                                 Length(min=8, max=64),
                                 EqualTo('confirm_password', message='Passwords must match')
                             ])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8)])
