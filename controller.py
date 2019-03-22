import data as d

import os

# bin_path = "/usr/bin"
sensortool = "sensortool"
powertool = "powertool"
fan = "fan"


def cmd_call(cmd: str):
    return os.system(cmd)


def get_sensor_data(node_num):
    """
    @TODO
    > 각 명령어에 맞춰 수정할 것
    """
    # data = cmd_call("sensortool --get-sensor-data --nude-num={}".format(node_num))
    data = {"node_num": node_num, "test_data": "get_sensor_data func"}
    return data


def get_fan_mode(fan_id: int):
    # data = cmd_call("sensortool --get-fan-mode --fan-id={}".format(fan_id))
    data = {"fan_id": fan_id, "test_data": "get_fan_mode func"}
    return data


def set_fan_mode(fan_id: int, fan_mode: int) -> int:
    # cmd_call("sensortool --set-fan-mode={} --fan-id={}".format(fan_mode, fan_id))
    print(fan_id, fan_mode)
    result_state = 1
    return result_state


def run_power_tool(tag: str) -> int:
    # cmd_call("powertool --tag={}".format(tag))
    print(tag)
    result_state = 1
    return result_state
