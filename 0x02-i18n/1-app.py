#!/usr/bin/env python3
"""Basic Bebel setup"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Contains supported Languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object('1-app.Config')
babel = Babel(app)


@app.route('/')
def home():
    """Renders Home Page"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
