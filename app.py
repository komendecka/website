from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)


@app.route('/me')
def me_page():
    return render_template("me.html")


@app.route('/contact')
def contact():
    return render_template("kontakt.html")
