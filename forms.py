import models

from flask.ext.mongoengine.wtf import model_form
from wtforms.fields import *
from wtforms import StringField, BooleanField, DateTimeField, TextField, PasswordField, Form, validators

user_form = model_form(models.User, exclude=['password'])

# Sigup Form created from user_form
class SignupForm(user_form):
	password = PasswordField('Password', validators=[validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
	confirm = PasswordField('Repeat Password')

#Login form will provide a Password field (WTForm form field)
class LoginForm(user_form):
	password = PasswordField('Password', validators=[validators.Required()])
