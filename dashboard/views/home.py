from flask import Blueprint, render_template, current_app

home = Blueprint("home", __name__, url_prefix='/')

@home.route("/")
def index():
    return render_template("index.html")