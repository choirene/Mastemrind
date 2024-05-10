from flask import Blueprint, Flask, render_template

index_bp = Blueprint("index", __name__)
home_bp = Blueprint("home", __name__)

@index_bp.route("/index", methods=["GET"])
def index():
    intro_text = "Hello, World!"
    return intro_text
@home_bp.route("/", methods=["GET"])
def home():
    # message = "Welcome to Mastermind!!!"
    # return render_template('index.html', message=message)

    home_text = "Welcome to Mastermind"
    return home_text
