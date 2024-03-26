from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt
from point import Point

class Axis(QWidget):
    def __init__(self, parent=None):
        super(Axis, self).__init__(parent)
        self.center = Point(0, 0, 0)
        self.ox = Point(900, 0, 0)
        self.oy = Point(0, 900, 0)
        self.oz = Point(0, 0, 900)

    def tostart(self):
        self.center = Point(0, 0, 0)
        self.ox = Point(900, 0, 0)
        self.oy = Point(0, 900, 0)
        self.oz = Point(0, 0, 900)

    def rotate(self, ax, ay, az):
        self.ox.rotateX(ax)
        self.ox.rotateY(ay)
        self.ox.rotateZ(az)
        self.oy.rotateX(ax)
        self.oy.rotateY(ay)
        self.oy.rotateZ(az)
        self.oz.rotateX(ax)
        self.oz.rotateY(ay)
        self.oz.rotateZ(az)

    def render(self, scene):
        scene.setColor(QColor.red)
        scene.drawLine(self.center, self.ox)
        scene.setColor(QColor(0, 155, 0))
        scene.drawLine(self.center, self.oy)
        scene.setColor(QColor.black)
        scene.drawLine(self.center, self.oz)

