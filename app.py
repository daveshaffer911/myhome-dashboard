from flask import Flask, flash, redirect, render_template, request, session, abort,jsonify
import os
import json

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


@app.route("/")
def index():
    #rates = getExchangeRates()
    return render_template('dashboard.html', **locals())

if __name__ == "__main__":
    app.run(debug=True)