from libs.simulation import Simulation
from typing import List
from .mat import Vektor
import cv2, math

class GUIObject:
    def __init__(self) -> None:
        self.Position = Vektor(0, 0)
        self.Size = Vektor(100, 20)
        self.Color = (0, 0, 0)
        self.Visibled = True
    
    def __call__(self, *args, **kwds) -> None:
        if self.Visibled:
            self.Call(kwds["f"])
            # kwds["f"] = cv2.rectangle(kwds["f"], self.Position.T, (self.Position + self.Size).T, self.color, 1, cv2.LINE_AA)
    
    def Call(self, frame) -> None:
        frame = cv2.rectangle(frame, self.Position.T, (self.Position + self.Size).T, self.Color, 1, cv2.LINE_AA)

class GUI:
    def __init__(self, simulation: Simulation) -> None:
        self.Objects: List[GUIObject] = []
        self.Simulation: Simulation = simulation
    
    
    def AddObject(self, obj):
        self.Objects.append(obj)
    
    def __call__(self, *args, **kwds) -> None:
        self.Simulation(kwds["f"]) 
        for obj in self.Objects:
            obj(**kwds)
    


class Label(GUIObject):

    def __init__(self, text: str) -> None:
        super().__init__()
        self.Text = text
        self.Font_size = .5
        self.Weight = 1
    
    def Call(self, frame) -> None:
        frame = cv2.putText(frame, self.Text, self.Position.int(), cv2.FONT_HERSHEY_SIMPLEX , self.Font_size, self.Color, self.Weight, cv2.LINE_AA)
    
    def size(self):
        return cv2.getTextSize(self.Text, cv2.FONT_HERSHEY_SIMPLEX, self.Font_size, self.Weight)
    

class Drawing:

    @staticmethod
    def Rectangle(frame, position: Vektor, size: Vektor, angle: float, color: tuple, thickness: float=5) -> None:
            center_point = position // 1
            p_lt = Drawing.RotatePoint(position - size/2, angle, center_point)
            p_lb = Drawing.RotatePoint(position + Vektor(-1, 1) * size/2, angle, center_point)
            p_rt = Drawing.RotatePoint(position + Vektor(1, -1) * size/2, angle, center_point)
            p_rb = Drawing.RotatePoint(position + size/2, angle, center_point)
            # print(p_lt, p_lb, p_rt, p_rb)
            frame = cv2.line(frame, p_lt.int(), p_rt.int(), color, thickness)
            frame = cv2.line(frame, p_lt.int(), p_lb.int(), color, thickness)
            frame = cv2.line(frame, p_rt.int(), p_rb.int(), color, thickness)
            frame = cv2.line(frame, p_lb.int(), p_rb.int(), color, thickness)
            # frame = cv2.line(frame, (x, y), (x + w, y + h), color, 1)
    
    @staticmethod
    def Circle(frame, position: Vektor, radius: int, color: tuple, thickness: float) -> None:
        frame = cv2.circle(frame, position.int(), radius, color, thickness)

    @staticmethod
    def RotatePoint(position: Vektor, angle: float, centerPoint: Vektor)-> Vektor:
        pp = position - centerPoint
        return Vektor(int(pp.T[0]*math.cos(angle) - pp.T[1]*math.sin(angle)), int(pp.T[0]*math.sin(angle) + pp.T[1]*math.cos(angle))) + centerPoint