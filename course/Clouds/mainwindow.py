import time

from PyQt6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PyQt6.QtCore import Qt
from PyQt6.uic.properties import QtWidgets
from PySide6.QtWidgets import QWidget

from constants import CW, CH
from myscene import Scene
from axis import Axis
from cloud import Cloud
from camera import Camera
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.myScene = Scene()
        self.xyz = Axis()
        size = 0.1
        x = 50
        y = 50
        z = 50
        d = 0
        self.generateCloud = Cloud(size, x, y, z, d)
        self.grid = None
        self.densityDelta = 0
        self.density = 0.9

        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        # TODO: Setup the UI elements and initial scene setup here
        self.generateCloud = Cloud(0.1, 50, 50, 50, 0)  # Initialize generateCloud here
        self.ui.draw_label.setPixmap(self.myScene.getPixmap())

    def setup_connections(self):
        # TODO: Connect signals and slots for UI elements here
        pass
        # self.ui.pushButton_2.clicked.connect(self.test)
        # self.ui.clear_button.clicked.connect(self.on_clear_button_clicked)
        # self.ui.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        # self.ui.densitySlider.valueChanged.connect(self.on_densitySlider_valueChanged)
        # self.ui.button_size.clicked.connect(self.on_button_size_clicked)
        # self.ui.clear_button_2.clicked.connect(self.on_clear_button_2_clicked)
        # self.ui.button_exsample_2.clicked.connect(self.on_button_exsample_2_clicked)
        # self.ui.button_exsample_3.clicked.connect(self.on_button_exsample_3_clicked)
        # self.ui.button_exsample_4.clicked.connect(self.on_button_exsample_4_clicked)
        # self.ui.action.triggered.connect(self.on_action_triggered)
        # self.ui.action_2.triggered.connect(self.on_action_2_triggered)
        # self.ui.action_4.triggered.connect(self.on_action_4_triggered)

    def keyPressEvent(self, event):
        key = event.key()

        if key not in [Qt.Key.Key_S, Qt.Key.Key_W, Qt.Key.Key_A, Qt.Key.Key_D,
                       Qt.Key.Key_E, Qt.Key.Key_Z, Qt.Key.Key_U, Qt.Key.Key_J,
                       Qt.Key.Key_H, Qt.Key.Key_K, Qt.Key.Key_N, Qt.Key.Key_I,
                       Qt.Key.Key_Plus, Qt.Key.Key_Minus]:
            return

        if key == Qt.Key.Key_S:
            self.myScene.alphax -= 5
        elif key == Qt.Key.Key_D:
            self.myScene.alphay -= 5
        elif key == Qt.Key.Key_A:
            self.myScene.alphay += 5
        elif key == Qt.Key.Key_W:
            self.myScene.alphax += 5
        elif key == Qt.Key.Key_E:
            self.myScene.alphaz += 5
        elif key == Qt.Key.Key_Z:
            self.myScene.alphaz -= 5
        elif key == Qt.Key.Key_Plus:
            self.myScene.k *= 1.2
        elif key == Qt.Key.Key_Minus:
            self.myScene.k *= 5 / 6
        elif key == Qt.Key.Key_H:
            self.myScene.dx -= 10
        elif key == Qt.Key.Key_K:
            self.myScene.dx += 10
        elif key == Qt.Key.Key_U:
            self.myScene.dy += 10
        elif key == Qt.Key.Key_J:
            self.myScene.dy -= 10
        elif key == Qt.Key.Key_I:
            self.myScene.dz += 10
        elif key == Qt.Key.Key_N:
            self.myScene.dz -= 10

        self.ui.draw_label.clear()
        self.myScene.clear()
        self.renderFromCache()
        self.ui.draw_label.setPixmap(self.myScene.getPixmap())

    def on_clear_button_clicked(self):
        # TODO: Implement the 'Clear' button clicked logic here
        pass

    def on_pushButton_2_clicked(self):
        density = 0
        self.ui.draw_label.clear()
        self.myScene.clear()
        self.generateCloud.generateVoxelGridRandom(18)

        print("generate DONE")

        grid = self.generateCloud.getGrid()
        self.generateCloud.putPointsToCache(0)
        self.renderFromCache()
        self.ui.draw_label.setPixmap(self.myScene.getPixmap())

        self.ui.main_list.clear()
        self.ui.main_list.append(f"Размер окна: {CW}x{CH}")
        self.ui.main_list.append(f"Размер облака: {grid.get_max_x()}x{grid.get_max_y()}x{grid.get_max_z()}")
        self.ui.main_list.append(f"Всего вокселей: {grid.get_max_x() * grid.get_max_y() * grid.get_max_z()}")
        self.ui.main_list.append(f"Из них значимых: {self.generateCloud.cacheCount()}")

    def on_densitySlider_valueChanged(self, value):
        densityDelta = -value / 200.0

        self.ui.draw_label.clear()
        self.myScene.clear()

        self.generateCloud.putPointsToCache(self.density + densityDelta)
        self.renderFromCache()
        self.ui.draw_label.setPixmap(self.myScene.getPixmap())

        grid = self.generateCloud.getGrid()
        self.ui.main_list.clear()
        self.ui.main_list.append(f"Размер окна: {CW}x{CH}")
        self.ui.main_list.append(f"Размер облака: {grid.get_max_x()}x{grid.get_max_y()}x{grid.get_max_z()}")
        self.ui.main_list.append(f"Всего вокселей: {grid.get_max_x() * grid.get_max_y() * grid.get_max_z()}")
        self.ui.main_list.append(f"Из них значимых: {self.generateCloud.cacheCount()}")

    def on_button_size_clicked(self):
        density = 0.9
        yy = self.ui.y_spin.value()
        xx = self.ui.x_spin.value()
        zz = self.ui.z_spin.value()

        self.ui.draw_label.clear()
        self.myScene.clear()

        self.generateCloud.generatevoxelgridrandom(18, xx, yy, zz)
        print("generate DONE")

        self.generateCloud.putPointsToCache(density + self.densityDelta)

        grid = self.generateCloud.getGrid()
        self.ui.main_list.clear()
        self.ui.main_list.append(f"Размер окна: {CW}x{CH}")
        self.ui.main_list.append(f"Размер облака: {grid.get_max_x()}x{grid.get_max_y()}x{grid.get_max_z()}")
        self.ui.main_list.append(f"Всего вокселей: {grid.get_max_x() * grid.get_max_y() * grid.get_max_z()}")
        self.ui.main_list.append(f"Из них значимых: {self.generateCloud.cacheCount()}")

        self.renderFromCache()

    def on_clear_button_2_clicked(self):
        self.myScene.init()
        self.ui.draw_label.clear()
        self.myScene.clear()
        self.renderFromCache()
        self.ui.draw_label.setPixmap(self.myScene.getPixmap())

    def on_button_exsample_2_clicked(self):
        self.ui.y_spin.setValue(30)
        self.ui.x_spin.setValue(100)
        self.ui.z_spin.setValue(100)
        self.myScene.alphax = 90
        self.on_button_size_clicked()
        self.ui.densitySlider.setValue(20)

    def on_button_exsample_3_clicked(self):
        self.ui.y_spin.setValue(30)
        self.ui.x_spin.setValue(100)
        self.ui.z_spin.setValue(100)
        self.myScene.alphax = 90
        self.on_button_size_clicked()
        self.ui.densitySlider.setValue(-18)

    def on_button_exsample_4_clicked(self):
        self.ui.y_spin.setValue(30)
        self.ui.x_spin.setValue(100)
        self.ui.z_spin.setValue(100)
        self.myScene.dz = -50
        self.myScene.k = 1.2 ** 4
        self.on_button_size_clicked()

    def on_action_triggered(self):
        dialog = QFileDialog()
        fname, _ = dialog.getOpenFileName()

        if not fname:
            return

        filename = fname
        self.generateCloud.readFromFile(filename)

        self.ui.draw_label.clear()
        self.myScene.clear()
        print("generate DONE")

        grid = self.generateCloud.getGrid()
        self.ui.main_list.clear()
        self.ui.main_list.append(f"Размер окна: {CW}x{CH}")
        self.ui.main_list.append(f"Размер облака: {grid.get_max_x()}x{grid.get_max_y()}x{grid.get_max_z()}")
        self.ui.main_list.append(f"Всего вокселей: {grid.get_max_x() * grid.get_max_y() * grid.get_max_z()}")
        self.ui.main_list.append(f"Из них значимых: {self.generateCloud.cacheCount()}")

        self.renderFromCache()

    def on_action_2_triggered(self):
        dialog = QFileDialog()
        fname, _ = dialog.getSaveFileName()

        if not fname:
            return

        filename = fname
        self.generateCloud.saveToFile(filename)

    def on_action_4_triggered(self):
        msg = QMessageBox()
        msg.setText("Клавиши W/S предназначены для вращения облака вокруг оси OX.\n"
                    "Клавиши A/D предназначены для вращения облака вокруг оси OY.\n"
                    "Клавиши Z/E предназначены для вращения облака вокруг оси OZ.\n"
                    "Клавиши H/K предназначены для перемещения облака по оси OX.\n"
                    "Клавиши J/U предназначены для перемещения облака по оси OY.\n"
                    "Клавиши N/I предназначены для перемещения облака по оси OZ.\n"
                    "Клавиши +/- предназначены для масштабирования облака относительно начала координат.")
        msg.exec()


    def liting(self):
        # TODO: Implement the lighting logic here
        pass

    def renderGrid(self):
        # TODO: Implement the grid rendering logic here
        pass

    def renderFromCache(self):
        self.generateCloud.renderFromCache(self.myScene)
        self.ui.draw_label.setPixmap(self.myScene.getPixmap())
        self.ui.settings_list.clear()
        self.ui.settings_list.append("k = " + str(self.myScene.k))
        self.ui.settings_list.append("dx = " + str(self.myScene.dx))
        self.ui.settings_list.append("dy = " + str(self.myScene.dy))
        self.ui.settings_list.append("dz = " + str(self.myScene.dz))
        self.ui.settings_list.append("alphax = " + str(self.myScene.alphax))
        self.ui.settings_list.append("alphay = " + str(self.myScene.alphay))
        self.ui.settings_list.append("alphaz = " + str(self.myScene.alphaz))

    def test(self):
        density = 0.9
        densityDelta = 0

        with open("time.txt", "w") as f:
            f.write(f"%5s,%10s,%10s,%10s\n" % ("N", "1", "2", "-"))
            print(f"%5s,%10s,%10s,%10s\n" % ("N", "1", "2", "-"))

            repeat = 10
            start = 120
            end = 150
            step = 10

            for i in range(start, end, step):
                f.write(f"%5d," % (i * i * i))
                print(f"%5d," % (i * i * i))

                time_total = 0
                for j in range(repeat):
                    start_time = time.process_time()
                    self.generateCloud.generatevoxelgridrandom(18, i, i, i)
                    end_time = time.process_time()
                    time_total += end_time - start_time
                average_time = time_total / repeat
                print(f"%10d," % average_time)
                f.write(f"%10d," % average_time)

                self.generateCloud.putPointsToCache(density + densityDelta)
                grid = self.generateCloud.getGrid()

                cache_count = self.generateCloud.cacheCount()
                print(f"%10d," % cache_count)
                f.write(f"%10d," % cache_count)

                time_total = 0
                for j in range(repeat):
                    start_time = time.process_time()
                    self.renderFromCache()
                    end_time = time.process_time()
                    time_total += end_time - start_time
                average_time = time_total / repeat
                print(f"%10d,\n" % average_time)
                f.write(f"%10d,\n" % average_time)

        print("File 'time.txt' created.")
