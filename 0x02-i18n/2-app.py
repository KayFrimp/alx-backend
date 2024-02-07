#!/usr/bin/env python3
"""Get locale from request"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Contains supported Languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object('2-app.Config')
babel = Babel(app)


@babel.locale_selector
def get_locale() -> str:
    """Determines the best match for supported Languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> str:
    """Renders Home Page"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
