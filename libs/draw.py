
import math, cv2
from typing import Tuple

def rotatePoint(p:Tuple[float, float], angle: float, centerPoint:Tuple[int, int]=(0,0))-> Tuple[float, float]:
    pp = p[0] - centerPoint[0], p[1] - centerPoint[1]
    return (int(pp[0]*math.cos(angle) - pp[1]*math.sin(angle)) + centerPoint[0], int(pp[0]*math.sin(angle) + pp[1]*math.cos(angle))+ centerPoint[1])


def rectangle(frame, x,y,w,h,a, color, thickness=5):
    center_point = (int(x), int(y))
    p_lt = rotatePoint((x - w/2, y - h/2), a, center_point)
    p_lb = rotatePoint((x - w/2, y + h/2), a, center_point)
    p_rt = rotatePoint((x + w/2, y - h/2), a, center_point)
    p_rb = rotatePoint((x + w/2, y + h/2), a, center_point)
    # print(p_lt, p_lb, p_rt, p_rb)
    frame = cv2.line(frame, p_lt, p_rt, color, thickness)
    frame = cv2.line(frame, p_lt, p_lb, color, thickness)
    frame = cv2.line(frame, p_rt, p_rb, color, thickness)
    frame = cv2.line(frame, p_lb, p_rb, color, thickness)
    # frame = cv2.line(frame, (x, y), (x + w, y + h), color, 1)


