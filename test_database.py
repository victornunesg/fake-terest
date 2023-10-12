# file to run some tests in local database, not necessary to run the app
from myproject import app, database
from myproject.models import User, Photo

with app.app_context():
    database.create_all()  # creating database