# -*- coding: utf-8 -*-

"""
 Created by IntelliJ IDEA.
 Project: Vraptor-Interpreter
 ===========================================
 User: ByeongGil Jung
 Date: 2019-03-16
 Time: 오후 5:06
"""

from flask import Flask, Response

import querycontroller as qc
import json

app = Flask(__name__)


@app.route("/")
def index():
    return "Vraptor Interpreter"


@app.route("/get_sensor_data")
def get_sensor_data():
    data = qc.get_sensor_data()
    res = json.dumps(data)
    return Response(res, status=200, mimetype="application/json")


@app.route("/get_fan_mode")
def get_fan_mode():
    data = qc.get_fan_mode()
    res = json.dumps(data)
    return Response(res, status=200, mimetype="application/json")


@app.route("/set_fan_mode")
def set_fan_mode():
    qc.set_fan_mode()


@app.route("/rum_power_tool")
def run_power_tool():
    qc.run_power_tool()


if __name__ == "__main__":
    app.run(port=7788, debug=True)
