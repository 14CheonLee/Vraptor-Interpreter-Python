# -*- coding: utf-8 -*-

"""
 Created by IntelliJ IDEA.
 Project: Vraptor-Interpreter
 ===========================================
 User: ByeongGil Jung
 Date: 2019-03-16
 Time: 오후 5:06
"""

from flask import Flask, Response, request

import controller as qc
import json

app = Flask(__name__)


@app.route("/")
def index():
    return "Vraptor Interpreter"


@app.route("/get_sensor_data", methods=["POST"])
def get_sensor_data():
    node_num = request.form["node_num"]

    data = qc.get_sensor_data(node_num=node_num)
    res = json.dumps(data)
    return Response(res, status=200, mimetype="application/json")


@app.route("/get_fan_mode", methods=["POST"])
def get_fan_mode():
    fan_id = request.form["fan_id"]

    data = qc.get_fan_mode(fan_id=fan_id)
    res = json.dumps(data)
    return Response(res, status=200, mimetype="application/json")


@app.route("/set_fan_mode", methods=["POST"])
def set_fan_mode():
    fan_id = request.form["fan_id"]
    fan_mode = request.form["fan_mode"]

    qc.set_fan_mode(fan_id=fan_id, fan_mode=fan_mode)


@app.route("/rum_power_tool", methods=["POST"])
def run_power_tool():
    tag = request.form["tag"]

    qc.run_power_tool(tag=tag)


if __name__ == "__main__":
    app.run(port=7788, debug=True)
