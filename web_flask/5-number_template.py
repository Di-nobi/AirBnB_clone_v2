#!/usr/bin/python3
""" A script that displays Python is cool """
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes=False

@app.route('/')
def hello_hbnb():
    """ Prints out to the web """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """ Prints out to the web """
    return 'HBNB'

@app.route('/c/<text>')
def c_is_fun(text):
    """ Displays C fllowed by the value of the text """
    return 'C {}'.format(text.replace('_', ' '))
@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ Displays Python followed by the value of text variable """
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>')
def number(n):
    """ Prints out number """
    return '{:d} is a number'.format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
    """ displays html page """
    return render_template('5-number.html', number=n)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
