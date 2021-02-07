from typing import List
from .math import Vektor
import cv2

class GUIObject:
    def __init__(self) -> None:
        self.Position = Vektor(0, 0)
        self.Size = Vektor(100, 20)
        self.Visibled = True
    
    def __call__(self, *args, **kwds) -> None:
        if self.Visibled:
            self.call(kwds["f"])
            # kwds["f"] = cv2.rectangle(kwds["f"], self.Position.T, (self.Position + self.Size).T, self.color, 1, cv2.LINE_AA)
    
    def call(self, frame) -> None:
        frame = cv2.rectangle(frame, self.Position.T, (self.Position + self.Size).T, self.color, 1, cv2.LINE_AA)

class GUI:
    def __init__(self) -> None:
        self.objects: List[GUIObject] = []
    
    def AddObject(self, obj):
        self.objects.append(obj)
    
    def __call__(self, *args, **kwds) -> None:
        kwds["f"]
        for obj in self.objects:
            obj(**{"f": kwds["f"]})


class Label(GUIObject):

    def __init__(self, text: str) -> None:
        super().__init__()
        self.text = text
        self.color = (255, 255, 0)
        self.position = (0, 0)
        self.font_size = .5
        self.weight = 1
    
    # def __call__(self, *args, **kwds) -> None:
    #     kwds["f"] = cv2.putText(kwds["f"], self.text, self.position, cv2.FONT_HERSHEY_SIMPLEX , self.font_size, self.color, self.weight, cv2.LINE_AA)
    
    def call(self, frame) -> None:
        frame = cv2.putText(frame, self.text, self.position, cv2.FONT_HERSHEY_SIMPLEX , self.font_size, self.color, self.weight, cv2.LINE_AA)
    
    def size(self):
        return cv2.getTextSize(self.text, cv2.FONT_HERSHEY_SIMPLEX, self.font_size, self.weight)
        