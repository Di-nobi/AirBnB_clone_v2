#!/usr/bin/python3
""" Starting the Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def close_session():
    """ Closes storage """
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def state_cities():
    """ shows States and there cities """
    state_city = storage.all(state_city).values
    return render_template("8-cities_by_states.html", state_city=state_city)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
