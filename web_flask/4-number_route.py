#!/usr/bin/python3
"""task one starts flask web app"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hey_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def heybnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisntfun(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def weluvpy(text):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<n>', methods=['GET'], strict_slashes=False)
def number(n):
    if n is type(int):
        return ('{} is a number'.format(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
