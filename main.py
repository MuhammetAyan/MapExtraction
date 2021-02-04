from libs.shapes import drawObjects, initObjects
from typing import List
import cv2
import numpy as np
from libs.draw import *
from libs.shapes import *


shape = (500, 700, 3)
robot = {
    "position": (50,50),
    "size": (50,20),
    "angle": 0,
    "v": 0
}
objects: List[object] = initObjects(shape, 10)
mapframe = np.zeros(shape=(shape[0], shape[1]), dtype=np.uint8)
mapframe += 128

def _event(event, x, y, flags, param):
    params = {"point":(x,y)}
    if event == cv2.EVENT_LBUTTONDOWN:
        Tasks.append((ArrivalToGoal, [mapframe, x, y, robot]))
    elif event == cv2.EVENT_RBUTTONDOWN:
        pass
    elif event == cv2.EVENT_LBUTTONUP:
        pass


cv2.namedWindow("frame")
cv2.setMouseCallback("frame", _event)
Tasks = []
while True:
    frame = np.zeros(shape=shape, dtype=np.uint8)
    drawObjects(frame, objects)
    rectangle(frame, robot["position"][0],robot["position"][1],robot["size"][0],robot["size"][1],robot["angle"]* math.pi / 180, color=(255,0,0))
    sin_a = math.sin(deregee2radian(robot["angle"]))
    cos_a = math.cos(deregee2radian(robot["angle"]))
    robot["position"] = robot["position"][0] + cos_a * robot["v"], robot["position"][1] + sin_a * robot["v"]
    Lidar(frame, robot, mapframe)
    for task in Tasks:
        if task[0](*task[1]):
            Tasks.remove(task)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('map',mapframe)
    cv2.imshow('frame',frame)
    #q tuşuna basılırsa çıkılsın
    PRESS = cv2.waitKey(1) & 0xFF
    if PRESS == ord('w'):
        robot["v"] += 0.1
    if PRESS == ord('s'):
        robot["v"] -= 0.1
    if PRESS == ord('a'):
        robot["angle"] -= 3.7
    if PRESS == ord('d'):
        robot["angle"] += 3.7
    if PRESS == ord(' '):
        robot["v"] = 0
    if PRESS == 27:
        break

cv2.destroyAllWindows()