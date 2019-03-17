"""
 Created by IntelliJ IDEA.
 Project: Vraptor-Interpreter
 ===========================================
 User: ByeongGil Jung
 Date: 2019-03-16
 Time: 오후 5:50
"""

import data as controller

import os

# bin_path = "/usr/bin"
sensortool = "sensortool"
powertool = "powertool"
fan = "fan"


def cmd_call(cmd):
    return os.system(cmd)


def get_sensor_data(node_num):
    """
    @TODO
    > 각 명령어에 맞춰 수정할 것
    """
    data = cmd_call("sensortool --get-sensor-data --nude-num={}".format(node_num))
    return data


def get_fan_mode(fan_id: int):
    data = cmd_call("sensortool --get-fan-mode --fan-id={}".format(fan_id))
    return data


def set_fan_mode(fan_id: int, fan_mode: int) -> None:
    cmd_call("sensortool --set-fan-mode={} --fan-id={}".format(fan_mode, fan_id))


def run_power_tool(tag: str) -> None:
    cmd_call("powertool --tag={}".format(tag))
