from libs.gui import GUI, Label
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
        if len(Tasks) > 0:
            Tasks.remove(Tasks[-1])
    elif event == cv2.EVENT_LBUTTONUP:
        pass


gui = GUI()

lbl_task = Label(f"Gorev Sayisi: 0")
lbl_task.position = (0, 20)
gui.AddObject(lbl_task)

lbl_hiz = Label(f"Hiz: 0")
lbl_hiz.position = (150, 20)
gui.AddObject(lbl_hiz)

lbl_angle = Label(f"Aci: 0")
lbl_angle.position = (250, 20)
gui.AddObject(lbl_angle)

gui_show = False
map_show = False

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
    if len(Tasks) > 0:
        FirstTask, args = Tasks[0]
        if FirstTask(*args):
            Tasks.remove(Tasks[0])
        # frame = cv2.putText(frame, f"Args: {args[1]}, {args[2]}", (150, 20) , cv2.FONT_HERSHEY_SIMPLEX , .5, (255, 255, 0), 1, cv2.LINE_AA)
    beforePoint = int(robot["position"][0]), int(robot["position"][1])
    for task in Tasks:
        FirstTask, args = task
        frame = cv2.line(frame, pt1=beforePoint, pt2=(args[1], args[2]), color=(255,0,0), thickness=1)
        beforePoint = (args[1], args[2])
        # frame = cv2.circle(frame, (args[1], args[2]), radius=5, color=(255,255,0), thickness=-1)
    lbl_task.text = f"Gorev Sayisi: {len(Tasks)}"
    lbl_hiz.text = f"Hiz: {robot['v']}"
    lbl_angle.text = f"Aci: {robot['angle']}"
    if gui_show:
        gui(**{"f":frame})
    # frame = cv2.putText(frame, f"Gorev Sayisi: {len(Tasks)}", (0, 20) , cv2.FONT_HERSHEY_SIMPLEX , .5, (255, 255, 0), 1, cv2.LINE_AA)
    # frame = cv2.putText(frame, f"Hiz: {robot['v']}", (150, 20) , cv2.FONT_HERSHEY_SIMPLEX , .5, (255, 255, 0), 1, cv2.LINE_AA)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if map_show:
        cv2.imshow('map',mapframe)
    cv2.imshow('frame',frame)
    #q tuşuna basılırsa çıkılsın
    PRESS = cv2.waitKey(1) & 0xFF
    if PRESS == ord('1'):
        gui_show = not gui_show
    elif PRESS == ord('2'):
        map_show = not map_show
    elif PRESS == ord('w'):
        robot["v"] += 0.1
    elif PRESS == ord('s'):
        robot["v"] -= 0.1
    elif PRESS == ord('a'):
        robot["angle"] -= 3.7
    elif PRESS == ord('d'):
        robot["angle"] += 3.7
    elif PRESS == ord(' '):
        robot["v"] = 0
    elif PRESS == 27:
        break

cv2.destroyAllWindows()