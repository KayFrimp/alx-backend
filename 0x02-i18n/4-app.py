#!/usr/bin/env python3
"""Get locale from request"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Contains supported Languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)


app.config.from_object('4-app.Config')


@babel.localeselector
def get_locale():
    """Determines the best match for supported Languages"""
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """Renders Home Page"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
