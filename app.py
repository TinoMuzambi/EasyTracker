from flask import Flask, render_template
from datetime import date
import os
from easytracker.easytracker import EasyTracker

app = Flask(__name__)

@app.context_processor
def inject_year():
    return dict(year=date.today().year)

@app.route('/')
def home():
    tracker = EasyTracker()
    client = tracker.login(str(os.environ.get("EASY_USERNAME")), str(os.environ.get("EASY_PASSWORD")))
    accounts = tracker.get_accounts(client)
    return render_template("index.html", accounts=accounts)

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
