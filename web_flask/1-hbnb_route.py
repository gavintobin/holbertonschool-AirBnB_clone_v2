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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
