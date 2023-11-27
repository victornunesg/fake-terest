# file to run some tests in local database, not necessary to run the app
from myproject import app, database, bcrypt

from myproject.models import User, Photo

'''
registered users:

victor@gmail.com // yasmin@gmail.com
senha123

'''
# this file is used to do test with the database

# =====================================
# creates database according to the models, comment after run it for the first time
# =====================================
#
# with app.app_context():
#     database.create_all()

# =====================================
# clean tables from database
# =====================================

# with app.app_context():
#     database.drop_all()
