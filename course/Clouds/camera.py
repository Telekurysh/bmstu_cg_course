from constants import YCENTER, CH, XCENTER
from point import Point
from vector3 import Vector3

class Camera:
    def __init__(self):
        self.center = Point(0, 0, -YCENTER)
        self.d = YCENTER
        self.pov = 90
        self.Vh = CH
        self.Vw = CH
        self.up = Vector3(0, YCENTER, 0)
        self.straight = Vector3(0, 0, self.d)
        self.right = Vector3(XCENTER, 0, 0)

    def pointToCam(self, p):
        return Point(p.x() / XCENTER, p.y() / YCENTER, (p.z() + self.d) / self.d)

    def CamToScreenStandart(self, p):
        if p.z() == 0:
            return p
        p1 = Point()
        p1.setX(XCENTER + XCENTER * p.x() / p.z())
        p1.setY(YCENTER - YCENTER * p.y() / p.z())
        p1.setZ(p.z())
        return p1

    def ProjectVertex(self, p, r):
        if p.z() and (p.z() + self.d):
            r *= self.d / (p.z() + self.d)
        return self.CamToScreenStandart(self.pointToCam(p))

    def inCameraView(self, p):
        if p.z() < -self.d:
            return False
        return True
