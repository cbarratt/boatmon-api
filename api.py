import json
import sqlite3
import querydata

from flask import Flask
from flask import Response
from flask import g

app = Flask(__name__)

DATABASE = './boatmon.db'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()

@app.after_request
def after_request(response):
    g.db.close()

    return response

@app.route("/api/data")
def data():
    main = {}
    temperature_data = querydata.get_temperatures()
    voltage_data = querydata.get_voltages()

    main.update(temperature_data)
    main.update(voltage_data)

    json_data = json.dumps(main)

    return Response(json_data, mimetype='application/json')
