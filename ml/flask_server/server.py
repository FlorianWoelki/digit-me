import json
from flask import Flask
from flask import jsonify
from flask import send_file
from flask_cors import CORS

app = Flask(__name__, static_url_path='')
CORS(app)


@app.route('/model')
def get_model():
    return jsonify(read_json('../target/model.json'))


@app.route('/group1-shard1of1')
def get_group():
    return send_file('../target/group1-shard1of1')


def read_json(file):
    with open(file) as f:
        data = json.load(f)
    return data


app.run('0.0.0.0')
