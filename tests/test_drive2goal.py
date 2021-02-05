import sys, os
from typing import Tuple
sys.path.insert(1, os.path.join(os.getcwd()))

from pytest_bdd import scenarios, given, when, then, parsers
import libs.shapes as sh
import pytest
import math

scenarios('../features/drive2goal.feature')

pytest.robot = {
                "position": (0, 0),
                "size": (50,20),
                "angle": 0,
                "v": 0
            }
pytest.goal = (0, 0)


@given(parsers.parse('Robot position: ({x:d}, {y:d}), angle: {angle:d}'))
def set_robot(x, y, angle):
    pytest.robot["position"] = (x, y)
    pytest.robot["angle"] = angle


@when(parsers.parse('Mouse ile ({x:d}, {y:d}) noktasına tıklanınca'))
def set_goal(x, y):
    pytest.goal = (x, y)


@then(parsers.parse('Hedef varış durumu: "{result}". Açı değişme durumu: "{turn_pos}"'))
def kontrol(result, turn_pos):
    result = result == "True"
    x, y = pytest.goal
    first_angle = pytest.robot["angle"]
    r = sh.ArrivalToGoal(None, x, y, pytest.robot)
    delta_angle = (pytest.robot["angle"] - first_angle)
    _turn_pos = (delta_angle / abs(delta_angle)) if delta_angle != 0 else 0
    if turn_pos == "yok":
        turn_pos = 0
    elif turn_pos == "saat yonu":
        turn_pos = 1
    elif turn_pos == "saat yonunun tersi":
        turn_pos = -1
    else:
        raise "turn_pos bilinmeyen tipte!"
    assert r == result and _turn_pos == turn_pos