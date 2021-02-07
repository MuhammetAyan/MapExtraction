import sys, os
from typing import Tuple
sys.path.insert(1, os.path.join(os.getcwd()))

from pytest_bdd import scenarios, given, when, then, parsers
import libs.shapes as sh
import pytest
import math

scenarios('../../features/Lidar/LidarCenterPoint.feature')

pytest.robot = {
                "position": (0, 0),
                "size": (50,20),
                "angle": 0,
                "v": 0
            }
# pytest.LidarAngle = 0


@given(parsers.parse('Robot position: ({x:d}, {y:d})'))
def set_robot(x, y):
    pytest.robot["position"] = (x, y)

@given(parsers.parse('Angle: {angle:d}'))
def set_robot(angle):
    pytest.robot["angle"] = angle


@when(parsers.parse('Robot size: ({width:d}, {height:d})'))
def set_robot_size(width, height):
    pytest.robot["size"] = (width, height)


@then(parsers.parse('Center point: ({x:d}, {y:d})'))
def kontrol(x, y):
    assert sh.LidarCenterPoint(pytest.robot) == (x, y)