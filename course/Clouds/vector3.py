import math

from PyQt6.QtWidgets import QMessageBox
import time
from point import Point

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.vec = [x, y, z]

    def __getitem__(self, n):
        return self.vec[n]

    def __setitem__(self, n, value):
        self.vec[n] = value

    def length(self):
        return math.sqrt(self.length2())

    def length2(self):
        res = 0
        for v in range(len(self.vec)):
            # msg = QMessageBox()
            # a = str(type(v)) + '\n' + str(type(self.vec)) + '\n' + str(self.vec.__getitem__(v))
            # msg.setText(a)
            # msg.exec()
            # print(type(v), '\n', type(self.vec), '\n', type(self.vec[v]))
            res += self.vec[v] * self.vec[v]
        return res

    def normalize(self):
        length = self.length()
        return Vector3(v / length for v in self.vec)

    def __add__(self, other):
        return Vector3(self.vec[i] + other[i] for i in range(3))

    def __sub__(self, other):
        # msg = QMessageBox()
        # a = self.vec
        # msg.setText(str(a))
        # msg.exec()
        return Vector3(*list(self.vec[i] - other[i] for i in range(3)))

    def __mul__(self, other):
        if isinstance(other, Vector3):  # Dot product
            return sum(self.vec[i] * other[i] for i in range(3))
        else:  # Scalar multiplication
            return Vector3(self.vec[i] * other for i in range(3))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return Vector3(self.vec[i] / other for i in range(3))

    def __neg__(self):
        return Vector3(-self.vec[i] for i in range(3))

    def __iadd__(self, other):
        self.vec = [self.vec[i] + other[i] for i in range(3)]
        return self

    def __isub__(self, other):
        self.vec = [self.vec[i] - other[i] for i in range(3)]
        return self

    def __imul__(self, other):
        self.vec = [self.vec[i] * other for i in range(3)]
        return self

    def __itruediv__(self, other):
        self.vec = [self.vec[i] / other for i in range(3)]
        return self

    def __eq__(self, other):
        return all(self.vec[i] == other[i] for i in range(3))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"Vector3({self.vec[0]}, {self.vec[1]}, {self.vec[2]})"
