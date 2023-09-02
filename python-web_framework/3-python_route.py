#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that returns a greeting message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route that returns "HBNB".
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route that returns a string starting with 'C'
    followed by the value of the 'text' variable.
    The underscores in the 'text' variable are replaced with spaces.
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route that returns a string starting with 'Python'
    followed by the value of the 'text' variable.
    The underscores in the 'text' variable are replaced with spaces.
    If no value is provided for the 'text' variable, it defaults to 'is cool'.
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
