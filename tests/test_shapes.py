# libs klasörünün konumu import listesine ekleniyor.
import sys, os
from typing import Tuple
sys.path.insert(1, os.path.join(os.getcwd()))

import libs.shapes as sh
import pytest
import math

@pytest.mark.parametrize("deregee, radian", [
    (0, 0),
    (360, 2 * math.pi),
    (45, 2 * math.pi / 8),
    (90, 2 * math.pi / 4),
    (180, math.pi),
    (-90, -math.pi / 2)
    ])
def test_deregee2radian(deregee, radian):
    assert sh.deregee2radian(deregee) == radian


@pytest.mark.parametrize("deregee, radian", [
    (0, 0),
    (360, 2 * math.pi),
    (45, 2 * math.pi / 8),
    (90, 2 * math.pi / 4),
    (180, math.pi),
    (-90, -math.pi / 2)
    ])
def test_radian2deregee(deregee, radian):
    assert sh.radian2deregee(radian) == deregee


@pytest.mark.parametrize("x, y, xr, yr", [
    (0, 0, 0, 0),
    (0, 1, 0, 1),
    (1, 0, 1, 0),
    (1, 1, 0.7071067811865475, 0.7071067811865475),
    (7, 1, 0.9899494936611665, 0.1414213562373095),
    (-5,3, -0.8574929257125441, 0.5144957554275265),
    ])
def test_unit_vektor(x, y, xr, yr):
    _x, _y = sh._unit_vektor(x, y)
    assert _x == xr and _y == yr
