import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

users = [
    {'id': 1,
     'name': 'Janpreet Singh',
     'unique': 'DL935'},
    {'id': 2,
     'name': 'Second User',
     'unique': 'PBX'}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Singhventures Python API</h1><p>Prototype API for the coolest users.</p>"

@app.route('/api/v1/resources/users/all', methods=['GET'])
def api_all():
    return jsonify(users)

app.run()