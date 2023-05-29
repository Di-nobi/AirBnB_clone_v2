#!/usr/bin/python3
""" Starts the flask app """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False
@app.teardown_appcontext
def close_session():
    """ Closes storage """
    storage.close()
@app.route('/states_list', method=['GET'])
def all_states():
    """ Shows all states """
    all_state = storage.all(State).values
    return render_template("7-states_list.html", all_state=all_state)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
