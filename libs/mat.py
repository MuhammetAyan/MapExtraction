from typing import Callable, Tuple, Any
import math


class Vektor:
    def __init__(self, *args) -> None:
        self.T = (0, 0)
        if len(args) == 2:
            self.T = (args[0], args[1])
        elif type(args[0]) == tuple:
            self.T = args[0]
    
    def x(self) -> float:
        return self.T[0]
    
    def y(self) -> float:
        return self.T[1]
    
    def ix(self) -> int:
        return round(self.T[0])
    
    def iy(self) -> int:
        return round(self.T[1])
    
    def __str__(self) -> str:
        return f"<Vektor {self.T}>"
    
    def Length(self)-> float:
        """
        Vektörün uzunluğunu döndürür.
        """
        return math.sqrt(math.pow(self.T[0], 2) + math.pow(self.T[1], 2))
    
    def Select(self, *args) -> Tuple[Any, Any]:
        if len(args) == 1:
            return Vektor(args[0](self.T[0]), args[0](self.T[1]))
        elif len(args) == 2:
            return Vektor(args[0](self.T[0]), args[1](self.T[1]))
        else:
            raise "select args length be 1 or 2!"

    
    def int(self) -> Tuple[int, int]:
        return int(self.T[0]), int(self.T[1])
    
    def GetUnitVektor(self):
        """
        Bu vektörün birim vektörünü döndürür.
        """
        l = self.Length()
        if l == 0:
            return Vektor(0, 0)
        return Vektor(self.T[0] / l, self.T[1] / l)
    
    def GetAngle(self) -> float:
        """
        Vektörün orjine ile oluşturduğu açıyı radyan olarak verir.
        """
        return math.atan2(self.T[1], self.T[0])
    
    def __add__(self, other):
        if type(other) == Vektor:
            return Vektor(self.T[0] + other.T[0], self.T[1] + other.T[1])
        if type(other) in [int, float]:
            return Vektor(self.T[0] + other, self.T[1] + other)
    
    def __sub__(self, other):
        if type(other) == Vektor:
            return Vektor(self.T[0] - other.T[0], self.T[1] - other.T[1])
        if type(other) in [int, float]:
            return Vektor(self.T[0] - other, self.T[1] - other)
    
    def __rsub__(self, other):
        if type(other) == Vektor:
            return Vektor(other.T[0] - self.T[0], other.T[1] - self.T[1])
        if type(other) in [int, float]:
            return Vektor(other - self.T[0], other - self.T[1])
    
    def __mul__(self, other):
        if type(other) == Vektor:
            return Vektor(self.T[0] * other.T[0], self.T[1] * other.T[1])
        if type(other) in [int, float]:
            return Vektor(self.T[0] * other, self.T[1] * other)
    
    def __rmul__(self, other):
        if type(other) == Vektor:
            return Vektor(self.T[0] * other.T[0], self.T[1] * other.T[1])
        if type(other) in [int, float]:
            return Vektor(self.T[0] * other, self.T[1] * other)
    
    def __truediv__(self, other):
        if type(other) == Vektor:
            return Vektor(self.T[0] / other.T[0], self.T[1] / other.T[1])
        if type(other) in [int, float]:
            return Vektor(self.T[0] / other, self.T[1] / other)
    
    def __floordiv__(self, other):
        if type(other) == Vektor:
            return Vektor(self.T[0] // other.T[0], self.T[1] // other.T[1])
        if type(other) in [int, float]:
            return Vektor(self.T[0] // other, self.T[1] // other)
    
    def __rtruediv__(self, other):
        if type(other) == Vektor:
            return Vektor(other.T[0] / self.T[0] , other.T[1] / self.T[1])
        if type(other) in [int, float]:
            return Vektor(other / self.T[0], other / self.T[1])
    
    def __rfloordiv__(self, other):
        if type(other) == Vektor:
            return Vektor(other.T[0] // self.T[0] , other.T[1] // self.T[1])
        if type(other) in [int, float]:
            return Vektor(other // self.T[0], other // self.T[1])


class Angle:

    @staticmethod
    def Deregee2radian(deregee: float) -> float:
        """
        Dereceyi radyana çevirir.
        """
        return deregee * math.pi / 180

    @staticmethod
    def Radian2deregee(radian: float) -> float:
        """
        Radyanı dereceye çevirir.
        """
        return radian * 180 / math.pi
    
    @staticmethod
    def DiffAngle(a1: float, a2: float) -> float:
        """
        Verilen derece türündeki iki açı arasındaki mutlak değeri en küçük farkı (a2 - a1) hesaplar.
        """
        a1 %= 360
        a2 %= 360

        return min(
            a2 - a1,
            a2 - (a1 - 360),
            (a2 - 360) - a1,
            (a2 - 360) - (a1 - 360),
            key=abs
        )