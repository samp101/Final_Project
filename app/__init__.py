from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
import random


# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# Flask Mail Configuration
app.config['MAIL_SERVER']     = 'smtp.gmail.com'
app.config['MAIL_PORT']       = 587
app.config['MAIL_USE_TLS']    = True
app.config['MAIL_USE_SSL']    = False
app.config['MAIL_DEBUG']    = True
app.config['MAIL_USERNAME']   = 'myburg91@gmail.com'
app.config['MAIL_PASSWORD']  = 'Myburger1!'
app.config['MAIL_DEFAULT_SENDER'] = 'myburg91@gmail.com'
app.config['MAIL_PASSWORD']   = 'Myburger1!'

mail = Mail(app)


# Database Connection
db_info = {'host': 'localhost',
		   'database': 'burger2go',
		   'user': 'postgres',
		   'password': 'Tehilla1!',
		   'port': ''}

app.config[
	'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['password']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes
