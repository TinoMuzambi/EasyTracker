from flask import Flask, render_template
from datetime import date


app = Flask(__name__)

@app.context_processor
def inject_year():
    return dict(year=date.today().year)

@app.route('/')
def home():
    return render_template("index.html")\

@app.route('/about')
def about():
    return render_template("about.html")
