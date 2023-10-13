# file to define website routes/links
from flask import render_template, url_for, redirect
from myproject import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from myproject.forms import FormLogin, FormCreateAccount, FormPhoto
from myproject.models import User, Photo
from werkzeug.utils import secure_filename
import os


@app.route("/", methods=["GET", "POST"])  # creating a new route/link to your site
def homepage():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        user = User.query.filter_by(email=formlogin.email.data).first()
        if user and bcrypt.check_password_hash(user.password, formlogin.password.data):
            login_user(user)
            return redirect(url_for("profile", user_id=user.id))
    return render_template("homepage.html", form=formlogin)


@app.route("/createaccount", methods=["GET", "POST"])
def createaccount():
    formcreateaccount = FormCreateAccount()
    if formcreateaccount.validate_on_submit():
        encrypt_password = bcrypt.generate_password_hash(formcreateaccount.password.data)
        new_user = User(email=formcreateaccount.email.data, username=formcreateaccount.username.data,
                        password=encrypt_password)
        database.session.add(new_user)
        database.session.commit()
        login_user(new_user)
        return redirect(url_for("profile", user_id=new_user.id))
    return render_template("createaccount.html", form=formcreateaccount)


@app.route("/profile/<user_id>", methods=["GET", "POST"])  # pass a variable called 'usuario', to load a specific user page
@login_required
def profile(user_id):
    if int(user_id) == int(current_user.id):
        form_photo = FormPhoto()
        if form_photo.validate_on_submit():
            file = form_photo.photo.data
            safe_name = secure_filename(file.filename)
        return render_template("profile.html", user=current_user, form=form_photo)  # user is the same variable to use inside html file
    else:
        user = User.query.get(int(user_id))
        return render_template("profile.html", user=user, form=None)  # user is the same variable to use inside html file


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))
