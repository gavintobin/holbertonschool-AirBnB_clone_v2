#!/usr/bin/python3
"""9"""
from flask import Flask, request, render_template
from models import storage


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    '''9'''
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route('/states/<id>', strict_slashes=False)
def stateid(id):
    """9"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    '''9'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
