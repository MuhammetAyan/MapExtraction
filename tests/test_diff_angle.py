import sys, os
from typing import Tuple
sys.path.insert(1, os.path.join(os.getcwd()))

from pytest_bdd import scenarios, given, when, then, parsers
import libs.shapes as sh
import pytest
import math

scenarios('../features/DiffAngle.feature')

pytest.angle1 = 0
pytest.angle2 = 0


@given(parsers.parse('Angle1: {a:d}'))
def set_angle1(a):
    pytest.angle1 = a

@when(parsers.parse('Angle2: {a:d}'))
def set_angle1(a):
    pytest.angle2 = a

@then(parsers.parse('Diff: {diff:d}'))
def kontrol(diff):
    assert sh.DiffAngle(pytest.angle1, pytest.angle2) == diff
