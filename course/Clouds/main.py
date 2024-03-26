import sys
from PyQt6.QtWidgets import QApplication
from mainwindow import MainWindow

if __name__ == "__main__":
    sys.stdout = None  # Отключение буферизации вывода
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
