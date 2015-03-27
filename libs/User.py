import os

from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import LoginManager, current_user, login_required, login_user 
from flask.ext.login import logout_user, UserMixin, AnonymousUserMixin, confirm_login, fresh_login_required

import models

class User(UserMixin):
	def __init__(self, email=None, password=None, first_name=None, last_name=None, active=True, id=None ):
		self.email = email
		self.password = password
		self.first_name = first_name
		self.last_name = last_name
		self.active = active
		self.id = None

	

	def save(self):
		newUser = models.User(email=self.email, password=self.password, first_name=self.first_name, last_name=self.last_name, active=self.active)
		newUser.save()
		print "new user id = %s " % newUser.id
		self.id = newUser.id
		return self.id

	

	def get_by_email(self, email):
		dbUser = models.User.objects.get(email=email)
		if dbUser:
			self.email = dbUser.email
			self.active = dbUser.active
			self.id = dbUser.id
			return self
		else:
			return None

	

	def get_by_email_w_password(self, email):
		try:
			dbUser = models.User.objects.get(email=email)

			if dbUser:
				self.email = dbUser.email
				self.active = dbUser.active
				self.password = dbUser.password
				self.id = dbUser.id
				return self
			else:
				return None
		except:
			print "there was an error"
			return None

	

	def get_mongo_doc(self):
		if self.id:
			return models.User.objects.with_id(self.id)
		else:
			return None


	def get_by_id(self, id):
		dbUser = models.User.objects.with_id(id)
		if dbUser:
			self.email = dbUser.email
			self.active = dbUser.active
			self.id = dbUser.id
			self.first_name = dbUser.first_name
			self.last_name = dbUser.last_name

			return self
		else:
			return None

	class Anonymous(AnonymousUserMixin):
		name = "Anonymous"