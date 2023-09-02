#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"
  """
    Route: /
    Displays "Hello HBNB!" on the homepage.
    """

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"
  """
    Route: /hbnb
    Displays "HBNB" on the homepage.
    """

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace("_", " ")
    return "C {}".format(text)
  """
    Route: /c/<text>
    Displays "C_ " on the homepage.
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    