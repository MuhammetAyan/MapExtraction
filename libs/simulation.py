from typing import List
from . import gui
from .mat import Vektor, Angle
import math
import random
import numpy as np
from _thread import start_new_thread
import cv2

class Robot:
    
    def __init__(self) -> None:
        self.Position: Vektor = Vektor(50, 50)
        self.Size: Vektor = Vektor(50, 20)
        self.V:float = 0
        self.Angle: float = 0
        self._Rotation: List[Vektor] = []
        self.LidarLength: int = 250
        self.LidarAngle: int = 60
    
    def LidarScan(self, frame, mapframe)->None:
        """
        Anlık lidar taraması yapar.
        """
        centerPoint = self._LidarCenterPoint()
        for angle in range(-self.LidarAngle // 2, self.LidarAngle // 2 + 1, 5):
            # start_new_thread(self._LidarLaserThread, (frame, mapframe, angle, centerPoint))
            self._LidarLaserThread(frame, mapframe, angle, centerPoint)

    def _LidarCenterPoint(self) -> Vektor:
        """
        Lidar tarama ışınlarının yayılacağı noktayı hesaplar.
        """
        return self.Position + self.Size.x() // 2 * Vektor(math.cos(Angle.Deregee2radian(self.Angle)), math.sin(Angle.Deregee2radian(self.Angle))).Select(round)

    def _LidarLaserThread(self, frame, mapframe, laserAngle: int, center_point: Vektor) -> None:
        """
        Lidar taramanın bir ışın demetini hesaplar.
        """
        α = Angle.Deregee2radian(laserAngle)
        l = center_point - self.Position

        ll = Vektor(l.x() * math.cos(α) - l.y() * math.sin(α), l.x() * math.sin(α) + l.y() * math.cos(α)).GetUnitVektor()
        try:
            for l in range(1, self.LidarLength):
                lidar_vektor = ll * l
                e = lidar_vektor + self.Position // 1
                # ex, ey = (int(x + lidar_vektor[0]), int(y + lidar_vektor[1]))
                if e.x() >= frame.shape[1] or e.y() >= frame.shape[0] or e.x() < 0 or e.y() < 0:
                # if ex >= frame.shape[1] or ey >= frame.shape[0] or ex < 0 or ey < 0:
                    break
                color = [255, 255, 255]
                ok = True
                for c in range(3):
                    if frame[e.iy(), e.ix(), c] != color[c]:
                        ok = False
                        break
                if ok:
                    mapframe[e.iy(),e.ix()] = np.uint8(255)
                    break
                else:
                    mapframe[e.iy(),e.ix()] = np.uint8(0)
        except:
            pass
    
    def _Drive(self)-> None:
        """
        Robotun anlık hareketlerini düzenler. 
        """
        if len(self._Rotation) == 0: return
        # Direction Decide
        goal_angle = Angle.Radian2deregee((self._Rotation[0] - self.Position).GetAngle())
        # goal_angle = Angle.radian2deregee(math.atan2(y - robot["position"][1], x - robot["position"][0]))
        angle = Angle.DiffAngle(self.Angle, goal_angle)
        d = self._Rotation[0] - self.Position
        # dy, dx = (y - robot["position"][1], x - robot["position"][0])
        if d.x() != 0 or d.y() != 0:
            d_a = 0
            if angle <= -3:
                d_a = -3
            elif angle >= 3:
                d_a = 3
            elif angle > -3 and angle < 3:
                d_a = 0
                self.Angle = goal_angle
                assert self.Angle == goal_angle, f'{self.Angle} == {goal_angle}'
            self.Angle += d_a
        if angle == 0:
            self.V = 3
        else:
            self.V = 0
        # mapframe = cv2.line(mapframe, (int(robot["position"][0]), int(robot["position"][1])), (x, y), (50,), 3)
        if (self.Position - self._Rotation[0]).Length() < 3:
            self.V = 0
            self._Rotation.remove(self._Rotation[0])
        # Ana sürüş hareketi
        sin_a = math.sin(Angle.Deregee2radian(self.Angle))
        cos_a = math.cos(Angle.Deregee2radian(self.Angle))
        self.Position += Vektor(cos_a, sin_a) * self.V

    def _DrawRotation(self, frame) -> None:
        beforePoint = self.Position.int()
        for rota in self._Rotation:
            frame = cv2.line(frame, pt1=beforePoint, pt2=rota.int(), color=(255,0,0), thickness=1)
            beforePoint = rota.int()

    def __call__(self, *args, **kwds) -> None:
        """
        Robotu hareket ettirir. Ve ekrana çizer.
        """
        frame, mapFrame = args[0], args[1]
        self.LidarScan(frame, mapFrame)
        self._Drive()
        self._DrawRotation(frame)
        gui.Drawing.Rectangle(frame, self.Position, self.Size, Angle.Deregee2radian(self.Angle), color=(255,0,0))

    def AddGoal(self, position: Vektor) -> None:
        pass

    def AddRotation(self, position: Vektor) -> None:
        """
        Rota için yeni alt hedef noktası ekler.
        """
        self._Rotation.append(position)
    
    def RemoveRotation(self) -> None:
        """
        Rota için eklenmiş son alt hedef noktasını siler.
        """
        if len(self._Rotation) > 0:
            self._Rotation.remove(self._Rotation[-1])

class PhysicalObject:

    def __init__(self, position: Vektor, size: Vektor, _type: str, angle: float) -> None:
        self.Position: Vektor = position
        self.Size: Vektor = size
        self.Type: str = _type
        self.Angle: float = angle
    
    def __call__(self, *args, **kwds) -> None:
        frame = args[0]
        if self.Type == "rect":
            gui.Drawing.Rectangle(frame, self.Position, self.Size, self.Angle, color=(255,255,255))
        elif self.Type == "circle":
            frame = gui.Drawing.Circle(frame, self.Position, radius=self.Size.T[0], color=(255,255,255), thickness=-1)
        elif self.Type == "_rect":
            gui.Drawing.Rectangle(frame, self.Position, self.Size, self.Angle, color=(0, 0, 0))
        elif self.Type == "_circle":
            frame = gui.Drawing.Circle(frame, self.Position, radius=self.Size.T[0], color=(0, 0, 0), thickness=-1)


class Simulation:

    def __init__(self, physcial_size:tuple = (500, 700, 3)):
        self._Robots: List[Robot] = []
        self._Objects: List[PhysicalObject] = []
        self._Enabled: bool = False
        self.PhyscialSize: tuple = physcial_size
        self.MapFrame = None
    
    def DrawObjects(self, frame) -> None:
        for obj in self._Objects:
            obj(frame)

    def Start(self) -> None:
        self._Enabled = True

    def Stop(self) -> None:
        self._Enabled = False

    def Restart(self) -> None:
        self._Enabled = True
        self._Objects.clear()
        self._Objects.extend(Simulation._initObjects(self.PhyscialSize, 20))
        self.MapFrame = np.zeros(shape=self.PhyscialSize[:2], dtype=np.uint8)
        self.MapFrame += 128
        self._Robots.clear()
        self._Robots.append(Robot())

    @staticmethod
    def _initObjects(shape: tuple, objectNumber: int) -> List[PhysicalObject]:
        result = []
        for i in range(objectNumber):
            typ = random.choice(["rect", "circle", "_rect", "_circle"])
            position = Vektor(random.randint(0, shape[0]), random.randint(0, shape[1]))
            size = Vektor(random.randint(2, 150), random.randint(2, 150))
            a = Angle.Deregee2radian(random.randint(0,359))
            obj = PhysicalObject(position, size, typ, a)
            result.append(obj)
        return result
    
    def __call__(self, *args, **kwds):
        if self._Enabled:
            frame = args[0]
            self.DrawObjects(frame)
            for robot in self._Robots:
                robot(frame, self.MapFrame)