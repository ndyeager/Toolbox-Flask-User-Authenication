import os

from flask import Flask, render_template, request, redirect  # etc.
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import (current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required)

# Create and name Flask app
app = Flask("ToolboxApp")

# database connection
app.config['SECRET_KEY'] = 'afdskfdksgjdsfgjkdfjgdkgfdkgdkfgjf'
app.config['MONGODB_DB'] = 'toolbox'
app.config['MONGODB_HOST'] = 'mongodb://root:root@ds053080.mongolab.com:53080/toolbox'
app.debug = os.environ.get('DEBUG',True)

db = MongoEngine(app) # connect MongoEngine with Flask App
app.session_interface = MongoEngineSessionInterface(db) # sessions w/ mongoengine

# Flask BCrypt will be used to salt the user password
flask_bcrypt = Bcrypt(app)

# Associate Flask-Login manager with current app
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def index():
	return render_template("index.html")

@app.route("/user")
@login_required
def user_profile():
	return render_template("user_profile.html")

@app.route("/class")
@login_required
def class_page():
	return render_template("class.html")

@app.route('/student')
@login_required
def student_page():
	return render_template("student.html")