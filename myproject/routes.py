# file to define website routes/links
from flask import render_template, url_for, redirect, flash, request
from myproject import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from myproject.forms import FormLogin, FormCreateAccount, FormPhoto
from myproject.models import User, Photo
from wtforms import ValidationError
from werkzeug.utils import secure_filename
import os


@app.route("/", methods=["GET", "POST"])  # creating a new route/link to your site
def homepage():
    formlogin = FormLogin()
    if formlogin.validate_on_submit() and 'login_button' in request.form:
        user = User.query.filter_by(email=formlogin.email.data).first()
        if user and bcrypt.check_password_hash(user.password, formlogin.password.data):
            login_user(user)
            return redirect(url_for("profile", user_id=user.id))
        else:
            flash('Log in failure, wrong e-mail or password', 'alert-danger')
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
    if int(user_id) == int(current_user.id):  # if the current user is the logged user
        form_photo = FormPhoto()
        if form_photo.validate_on_submit():
            file = form_photo.photo.data
            safe_name = secure_filename(file.filename)  # making the filename secure to storage without crashing
            # salvar o arquivo na pasta
            file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),  # getting current file path folder
                                app.config["UPLOAD_FOLDER"],  # concatenating with static/posts_photos
                                safe_name)  # setting file name as secure file
            file.save(file_path)
            # registering photo in database
            photo = Photo(image=safe_name, user_id=current_user.id)
            database.session.add(photo)
            database.session.commit()
        return render_template("profile.html", user=current_user, form=form_photo)  # user is the same variable to use inside html file
    else:
        user = User.query.get(int(user_id))
        return render_template("profile.html", user=user, form=None)  # user is the same variable to use inside html file


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))


@app.route("/feed")
@login_required
def feed():
    photos = Photo.query.order_by(Photo.creation_date.desc()).all()
    return render_template("feed.html", photos=photos)
