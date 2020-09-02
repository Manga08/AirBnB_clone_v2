#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays Hello HBNB."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Displatys C <text>"""
    return 'C {}'.format(text).replace('_', ' ')


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def p_route(text):
    """Displatys Python <text>"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays n and a number."""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        data = "even"
    else:
        data = "odd"
    return render_template('6-number_odd_or_even.html', n=n, data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
