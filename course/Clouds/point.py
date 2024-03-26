import math
from matrix import Matrix
from constants import PI

class Point:
    def __init__(self, x=0, y=0, z=0):
        self.X = x
        self.Y = y
        self.Z = z

    def print(self):
        print(f"{self.X}, {self.Y}, {self.Z};")

    def x(self):
        return self.X

    def y(self):
        return self.Y

    def z(self):
        return self.Z

    def setY(self, y):
        self.Y = y

    def setX(self, x):
        self.X = x

    def setZ(self, z):
        self.Z = z

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.X == other.X and self.Y == other.Y and self.Z == other.Z

    def rotateX(self, a):
        if a == 0:
            return

        alpha = a * PI / 180
        m1 = Matrix(4, 4)
        m2 = Matrix(1, 4)

        m1.setMatrix([1, 0, 0, 0,
                      0, math.cos(alpha), -math.sin(alpha), 0,
                      0, math.sin(alpha), math.cos(alpha), 0,
                      0, 0, 0, 1])
        m2.setMatrix([self.x(), self.y(), self.z(), 1])

        res = m2 * m1
        self.setX(res[0][0])
        self.setY(res[0][1])
        self.setZ(res[0][2])

    def rotateY(self, a):
        if a == 0:
            return

        alpha = a * PI / 180
        m1 = Matrix(4, 4)
        m2 = Matrix(1, 4)

        m1.setMatrix([math.cos(alpha), 0, math.sin(alpha), 0,
                      0, 1, 0, 0,
                      -math.sin(alpha), 0, math.cos(alpha), 0,
                      0, 0, 0, 1])
        m2.setMatrix([self.x(), self.y(), self.z(), 1])

        res = m2 * m1
        self.setX(res[0][0])
        self.setY(res[0][1])
        self.setZ(res[0][2])

    def rotateZ(self, a):
        if a == 0:
            return

        alpha = a * PI / 180
        m1 = Matrix(4, 4)
        m2 = Matrix(1, 4)

        m1.setMatrix([math.cos(alpha), -math.sin(alpha), 0, 0,
                      math.sin(alpha), math.cos(alpha), 0, 0,
                      0, 0, 1, 0,
                      0, 0, 0, 1])
        m2.setMatrix([self.x(), self.y(), self.z(), 1])

        res = m2 * m1
        self.setX(res[0][0])
        self.setY(res[0][1])
        self.setZ(res[0][2])

    def move(self, dx, dy, dz):
        if dx == 0 and dy == 0 and dz == 0:
            return
        self.setX(self.X + dx)
        self.setY(self.Y + dy)
        self.setZ(self.Z + dz)

    def scaleUniform(self, c, k):
        x = c.x() + k * (self.x() - c.x())
        y = c.y() + k * (self.y() - c.y())
        z = c.z() + k * (self.z() - c.z())
        self.setX(x)
        self.setY(y)
        self.setZ(z)
