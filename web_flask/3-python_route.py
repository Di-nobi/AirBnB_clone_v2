#!/usr/bin/python3
""" A script that displays Python is cool """
from flask import Flask
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
def python_is_cool(text):
    """ Displays Python followed by the value of text variable """
    text = "is cool"
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
