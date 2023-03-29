#!/usr/bin/python3
"""task 8"""

from flask import Flask, request, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list/', strict_slashes=False)
def listthem():
    """88888"""
    states = storage.all('State')
    render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def storclo():
    """8 agaain"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
