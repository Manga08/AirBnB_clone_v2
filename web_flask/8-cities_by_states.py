#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__, template_folder='templates')


@app.teardown_appcontext
def app_context(abc):
    """Remove the current SQLAlchemy session."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """Display a HTML page inside the tag BODY."""
    return render_template('8-cities_by_states.html',
                           states=storage.all(State).values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
