import datetime
from app import db

class User(db.Document):
	username = db.StringField(max_length=35)
	email = db.StringField(unique=True, max_length=255)
	password = db.StringField(max_length=255)
	first_name = db.StringField(max_length=20)
	last_name = db.StringField(max_length=20)
	active = db.BooleanField(default=True)
	confirm_at = db.DateTimeField()