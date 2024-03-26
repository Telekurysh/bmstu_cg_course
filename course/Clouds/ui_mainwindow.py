# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6 import QtWidgets
from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PyQt6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QStatusBar,
    QTabWidget, QTextEdit, QToolBar, QVBoxLayout,
    QWidget)
from PyQt6.uic.properties import QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1250, 1000)
        self.action = QAction()
        self.action.setObjectName(u"action")
        self.action_2 = QAction()
        self.action_2.setObjectName(u"action_2")
        self.action_4 = QAction()
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction()
        self.action_5.setObjectName(u"action_5")
        self.centralWidget = QWidget()
        self.centralWidget.setObjectName(u"centralWidget")
        self.draw_label = QLabel(self.centralWidget)
        self.draw_label.setObjectName(u"draw_label")
        self.draw_label.setGeometry(QRect(30, 20, 900, 900))
        self.label = QLabel(self.centralWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(950, 90, 67, 17))
        self.verticalLayoutWidget = QWidget(self.centralWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(950, 20, 281, 901))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QSize(16777215, 243))
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 20, 221, 17))
        self.gridLayoutWidget = QWidget(self.tab_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 40, 241, 91))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.y_spin = QSpinBox(self.gridLayoutWidget)
        self.y_spin.setObjectName(u"y_spin")
        self.y_spin.setMinimum(1)
        self.y_spin.setMaximum(200)
        self.y_spin.setSingleStep(5)
        self.y_spin.setValue(30)

        self.gridLayout.addWidget(self.y_spin, 1, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.z_spin = QSpinBox(self.gridLayoutWidget)
        self.z_spin.setObjectName(u"z_spin")
        self.z_spin.setMinimum(1)
        self.z_spin.setMaximum(200)
        self.z_spin.setSingleStep(5)
        self.z_spin.setValue(100)

        self.gridLayout.addWidget(self.z_spin, 1, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.x_spin = QSpinBox(self.gridLayoutWidget)
        self.x_spin.setObjectName(u"x_spin")
        self.x_spin.setMinimum(1)
        self.x_spin.setMaximum(200)
        self.x_spin.setSingleStep(5)
        self.x_spin.setValue(100)

        self.gridLayout.addWidget(self.x_spin, 1, 0, 1, 1)

        self.button_size = QPushButton(self.gridLayoutWidget)
        self.button_size.setObjectName(u"button_size")

        self.gridLayout.addWidget(self.button_size, 2, 0, 1, 3)

        self.densitySlider = QSlider(self.tab_2)
        self.densitySlider.setObjectName(u"densitySlider")
        self.densitySlider.setGeometry(QRect(20, 170, 241, 20))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.densitySlider.sizePolicy().hasHeightForWidth())
        self.densitySlider.setSizePolicy(sizePolicy1)
        self.densitySlider.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.densitySlider.setFont(font)
        self.densitySlider.setMouseTracking(True)
        self.densitySlider.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.densitySlider.setMinimum(-20)
        self.densitySlider.setMaximum(20)
        self.densitySlider.setPageStep(1)
        self.densitySlider.setSliderPosition(0)
        self.densitySlider.setTracking(True)
        self.densitySlider.setOrientation(Qt.Orientation.Horizontal)
        self.densitySlider.setInvertedAppearance(False)
        self.densitySlider.setInvertedControls(False)
        self.densitySlider.setTickInterval(1)
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 150, 141, 17))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 10, 241, 41))
        self.button_exsample_2 = QPushButton(self.tab)
        self.button_exsample_2.setObjectName(u"button_exsample_2")
        self.button_exsample_2.setGeometry(QRect(20, 60, 241, 41))
        self.button_exsample_3 = QPushButton(self.tab)
        self.button_exsample_3.setObjectName(u"button_exsample_3")
        self.button_exsample_3.setGeometry(QRect(20, 110, 241, 41))
        self.button_exsample_4 = QPushButton(self.tab)
        self.button_exsample_4.setObjectName(u"button_exsample_4")
        self.button_exsample_4.setGeometry(QRect(20, 160, 241, 41))
        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 221))
        self.main_list = QTextEdit(self.groupBox)
        self.main_list.setObjectName(u"main_list")
        self.main_list.setEnabled(True)
        self.main_list.setGeometry(QRect(0, 20, 279, 200))
        self.main_list.setMaximumSize(QSize(16777215, 219))
        self.main_list.setReadOnly(True)

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 221))
        self.settings_list = QTextEdit(self.groupBox_2)
        self.settings_list.setObjectName(u"settings_list")
        self.settings_list.setEnabled(True)
        self.settings_list.setGeometry(QRect(0, 20, 279, 200))
        self.settings_list.setMaximumSize(QSize(16777215, 200))
        self.settings_list.setReadOnly(True)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.clear_button_2 = QPushButton(self.verticalLayoutWidget)
        self.clear_button_2.setObjectName(u"clear_button_2")
        self.clear_button_2.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.clear_button_2)

        self.clear_button = QPushButton(self.verticalLayoutWidget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.clear_button)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1250, 22))
        self.menuMybar = QMenu(self.menuBar)
        self.menuMybar.setObjectName(u"menuMybar")
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuMybar.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menuMybar.addAction(self.action)
        self.menuMybar.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MyCLoudRender", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u0444\u0430\u0439\u043b", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043d\u0430\u0441", None))
        self.draw_label.setText("")
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0440\u0430\u0437\u043c\u0435\u0440\u044b \u043e\u0431\u043b\u0430\u043a\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ysize:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Zsize:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Xsize:", None))
        self.button_size.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u044c \u043e\u0431\u043b\u0430\u043a\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0435", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0443\u0433\u043b\u043e\u0435 \u043e\u0431\u043b\u0430\u043a\u043e", None))
        self.button_exsample_2.setText(QCoreApplication.translate("MainWindow", u"Плотные облака", None))
        self.button_exsample_3.setText(QCoreApplication.translate("MainWindow", u"Разреженные облака", None))
        self.button_exsample_4.setText(QCoreApplication.translate("MainWindow", u"Пролет через облако", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0440\u044b", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0432\u044b\u0432\u043e\u0434\u0438\u043c\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432", None))
        self.clear_button_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043e\u0431\u0449\u0438\u0439 \u0432\u044b\u0432\u043e\u0434", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0432\u044b\u0432\u043e\u0434 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a", None))
        self.menuMybar.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
    # retranslateUi

