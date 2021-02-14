from libs.gui import GUI, Label

import cv2
import numpy as np
from libs.simulation import *

import os


sim = Simulation()
gui = GUI(sim)


lbl_info = Label(f"Gorev Sayisi: 0")
lbl_info.Position = Vektor(0, 20)
lbl_info.Color = (255, 200, 0)

gui.AddObject(lbl_info)

def input_task(task_count: int, v: float, angle: float):
    lbl_info.Text = f"Gorev Sayisi: {task_count}".ljust(17) + f"Hiz: {round(v, 3)}".ljust(9) + f"Aci: {round(angle, 3)}"

input_task(0, 0, 0)

sim.Restart()

def _event(event, x, y, flags, param):
    params = {"point":(x,y)}
    if event == cv2.EVENT_LBUTTONDOWN:
        sim._Robots[0].AddRotation(Vektor(x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        sim._Robots[0].RemoveRotation()
    elif event == cv2.EVENT_LBUTTONUP:
        pass


map_show = False

cv2.namedWindow("frame")
cv2.setMouseCallback("frame", _event)

while True:
    frame = np.zeros(shape=sim.PhyscialSize, dtype=np.uint8)
    gui(**{"f":frame})
    
    # sin_a = math.sin(Angle.deregee2radian(robot["angle"]))
    # cos_a = math.cos(Angle.deregee2radian(robot["angle"]))
    # robot["position"] += Vektor(cos_a, sin_a) * robot["v"]
    # Lidar(frame, robot, mapframe)
    # if len(Tasks) > 0:
    #     FirstTask, args = Tasks[0]
    #     if FirstTask(*args):
    #         Tasks.remove(Tasks[0])
    input_task(
        task_count=len(sim._Robots[0]._Rotation),
        v=sim._Robots[0].V,
        angle=sim._Robots[0].Angle
        )
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if map_show:
        cv2.imshow('map',sim.MapFrame)
    cv2.imshow('frame',frame)
    #q tuşuna basılırsa çıkılsın
    PRESS = cv2.waitKey(1) & 0xFF
    if PRESS == ord('1'):
        lbl_info.Visibled = not lbl_info.Visibled
    elif PRESS == ord('2'):
        map_show = not map_show
        cv2.destroyWindow("map")
    # elif PRESS == ord('w'):
    #     robot["v"] += 0.1
    # elif PRESS == ord('s'):
    #     robot["v"] -= 0.1
    # elif PRESS == ord('a'):
    #     robot["angle"] -= 3.7
    # elif PRESS == ord('d'):
    #     robot["angle"] += 3.7
    # elif PRESS == ord(' '):
    #     robot["v"] = 0
    elif PRESS == 27:
        break

cv2.destroyAllWindows()