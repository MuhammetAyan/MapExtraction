import math, cv2
from typing import List
import random
import numpy as np
from numpy.core.fromnumeric import shape
from numpy.lib.function_base import angle
from .draw import *

def deregee2radian(deregee: float) -> float:
    return deregee * math.pi / 180

def radian2deregee(radian: float) -> float:
    return radian * 180 / math.pi

class object:

    def __init__(self, x, y, w, h, type) -> None:
        self.type = type
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.a = 0

def initObjects(shape, objectNumber: int) -> List[object]:
    result = []
    for i in range(objectNumber):
        typ = random.choice(["rect", "circle", "_rect", "_circle"])
        x, y = random.randint(0, shape[0]), random.randint(0, shape[1])
        w, h = random.randint(2, 150), random.randint(2, 150)
        a = deregee2radian(random.randint(0,359))
        obj = object(x, y, w, h, typ)
        obj.a = a
        result.append(obj)
    return result


def drawObjects(frame, objects: List[object]):
    for obj in objects:
        if obj.type == "rect":
            rectangle(frame, obj.x, obj.y, obj.w, obj.h, obj.a, color=(255,255,255))
        elif obj.type == "circle":
            frame = cv2.circle(frame, (obj.x, obj.y), radius=obj.h, color=(255,255,255), thickness=-1)
        elif obj.type == "_rect":
            rectangle(frame, obj.x, obj.y, obj.w, obj.h, obj.a, color=(0, 0, 0))
        elif obj.type == "_circle":
            frame = cv2.circle(frame, (obj.x, obj.y), radius=obj.h, color=(0, 0, 0), thickness=-1)

def _vektor_length(x: float, y: float)-> float:
    return math.sqrt(math.pow(x,2) + math.pow(y, 2))

def _unit_vektor(x:float, y:float) -> Tuple[float, float]:
    b = _vektor_length(x, y)
    if b == 0:
        return 0, 0
    return x / b, y / b



def Lidar(frame, robot, mapframe) -> np.uint8:
    x, y = robot["position"]
    w, h = robot["size"]
    a = robot["angle"]
    v = robot["v"]
    tx = int(x + w // 2 * math.cos(deregee2radian(a)) + random.randint(-3, 3))
    ty = int(y + w // 2 * math.sin(deregee2radian(a)) + random.randint(-3, 3))
    # color =np.array([255, 255, 255], dtype=np.uint8)
    # for c in range(3):
    #     frame[ty, tx, c] = color[c]
    # lx, ly = _unit_vektor(tx - x, ty - y)
    # lidar_vektor = lx * 100, ly * 100
    # end_point = (int(x + lidar_vektor[0]), int(y + lidar_vektor[1]))
    # frame = cv2.line(frame, (tx, ty), end_point, (0,255,0))
    for angle in range(-40, 41, 5):
        α = deregee2radian(angle)
        lx, ly = tx - x, ty - y

        llx, lly = _unit_vektor(lx * math.cos(α) - ly * math.sin(α), lx * math.sin(α) + ly * math.cos(α))
        for l in range(1, 250):
            lidar_vektor = llx * l, lly * l
            ex, ey = (int(x + lidar_vektor[0]), int(y + lidar_vektor[1]))
            if ex >= frame.shape[1] or ey >= frame.shape[0] or ex < 0 or ey < 0:
                break
                return np.uint8(255)
            color = [255, 255, 255]
            ok = True
            for c in range(3):
                if frame[ey, ex, c] != color[c]:
                    ok = False
                    break
            if ok:
                mapframe[ey,ex] = np.uint8(255)
                # return np.uint8(l)
                break
            else:
                mapframe[ey,ex] = np.uint8(0)
    
    return np.uint8(255)

def ArrivalToGoal(mapframe, x: int, y: int, robot) -> bool:
    angle = radian2deregee(math.atan2(y - robot["position"][1], x - robot["position"][0])) - robot["angle"]
    d_a = 0
    if angle <= -3:
        d_a = -3
    elif angle >= 3:
        d_a = 3
    robot["angle"] += d_a
    robot["v"] = 1
    # mapframe = cv2.line(mapframe, (int(robot["position"][0]), int(robot["position"][1])), (x, y), (50,), 3)
    if abs(robot["position"][0] - x) < 5 and abs(robot["position"][1] - y) < 5:
        robot["v"] = 0
        return True
    else:
        return False