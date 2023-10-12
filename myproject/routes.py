# file to define website routes/links
from flask import render_template, url_for
from myproject import app
from flask_login import login_required


@app.route("/")  # creating a new route/link to your site
def homepage():
    return render_template("homepage.html")


@app.route("/perfil/<usuario>")  # pass a variable called 'usuario', to load a specific user page
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)  # usuario is the same variable to use inside html file
