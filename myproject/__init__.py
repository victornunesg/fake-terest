# file to define app, to create website, it says to PyCharm that this is a Flask Project
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)  # initiating Flask object, the app itself

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"  # configuring database local (standard)
app.config['SECRET_KEY'] = "da59332b26c23c31296ffad51bd953da"  # to make sure app security print(secrets.token_hex(16))

database = SQLAlchemy(app)  # creating database
bcrypt = Bcrypt(app)  # creating Bcrypt object
login_manager = LoginManager(app) # creating LoginManager object
login_manager.login_view = "homepage"  # specifying which route that manages the login, where to send not logged user

# importing other files necessary to app work properly, after app definition to avoid circular importation
from myproject import routes  # importing file routes inside myproject folder, to load the website links