from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtCore import Qt
from point import Point
from camera import Camera

background = QColor(190, 190, 255)


class Scene(QWidget):
    def __init__(self, parent=None):
        super(Scene, self).__init__(parent)
        self.scene = QPixmap(900, 900)
        self.scene.fill(background)

        self.painter = QPainter(self.scene)
        self.painter.setPen(background)
        self.clear_flag = True

        self.alphax = 0
        self.alphay = 0
        self.alphaz = 0
        self.k = 1
        self.dx = 0
        self.dy = 0
        self.dz = 0

        self.camera = Camera()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.label = QLabel()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def init(self):
        self.alphax = 0
        self.alphay = 0
        self.alphaz = 0
        self.k = 1
        self.dx = 0
        self.dy = 0
        self.dz = 0

    def clear(self):
        self.painter.end()
        self.scene = QPixmap(900, 900)
        self.scene.fill(QColor(background))
        self.painter = QPainter(self.scene)
        self.clear_flag = True

    def getPixmap(self):
        return self.scene

    def drawCircle(self, p, r, color=QColor.black):
        self.painter.setPen(color)
        self.clear_flag = False

        if self.alphax:
            p.rotateX(self.alphax)
        if self.alphay:
            p.rotateY(self.alphay)
        if self.alphaz:
            p.rotateZ(self.alphaz)
        if self.k != 1:
            p.scaleUniform(Point(0, 0, 0), self.k)
            r *= self.k
        if self.dx != 0 or self.dy != 0 or self.dz != 0:
            p.move(self.dx, self.dy, self.dz)
        if self.camera.inCameraView(p):
            p = self.camera.ProjectVertex(p, r)
            self.painter.setBrush(color)
            self.painter.drawEllipse(int(p.x()), int(p.y()), int(r), int(r))

    def drawPoint(self, p, color=QColor.black):
        self.painter.setPen(color)
        self.clear_flag = False
        r = 0
        if self.alphax:
            p.rotateX(self.alphax)
        if self.alphay:
            p.rotateY(self.alphay)
        if self.alphaz:
            p.rotateZ(self.alphaz)
        if self.k != 1:
            p.scaleUniform(Point(0, 0, 0), self.k)
        if self.camera.inCameraView(p):
            p = self.camera.ProjectVertex(p, r)
            self.painter.drawPoint(p.x(), p.y())

    def drawLine(self, p1, p2):
        self.clear_flag = False
        if self.alphax:
            p1.rotateX(self.alphax)
            p2.rotateX(self.alphax)
        if self.alphay:
            p1.rotateY(self.alphay)
            p2.rotateY(self.alphay)
        if self.alphaz:
            p1.rotateZ(self.alphaz)
            p2.rotateZ(self.alphaz)
        r = 0
        p1 = self.camera.ProjectVertex(p1, r)
        p2 = self.camera.ProjectVertex(p2, r)
        self.painter.drawLine(p1.x(), p1.y(), p2.x(), p2.y())

    def setColor(self, color):
        self.painter.setPen(color)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.scene)

    def resizeEvent(self, event):
        self.camera.setProjectionMatrix(self.width(), self.height())
        self.update()

    def keyPressEvent(self, event):
        # TODO: Implement the key press event logic here
        pass

