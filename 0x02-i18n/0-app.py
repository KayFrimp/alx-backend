#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    """Renders Home Page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
