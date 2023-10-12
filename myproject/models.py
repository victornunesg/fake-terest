# file to define database structure
from myproject import database as db, login_manager
from datetime import datetime
from flask_login import UserMixin  # says which class will manage login structure


# mandatory function whenever login structure is created, returns who the user is
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):  # it is a subclass of Model, from database
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    photos = db.relationship("Photo", backref="user", lazy=True)


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String, default="default.jpg")
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
