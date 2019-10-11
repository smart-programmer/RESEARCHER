from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "AAA2002AAA"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
# NOTE: the flask migration moudle/package database url must be relative to the file that will be run when migrating offline which in this case is run.py, that's why in the env file the directory is different then in here.

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'






from RESEARCHER import routes