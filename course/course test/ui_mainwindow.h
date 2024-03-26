/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.6.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSlider>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *action;
    QAction *action_2;
    QAction *action_4;
    QAction *action_5;
    QWidget *centralWidget;
    QLabel *draw_label;
    QLabel *label;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout;
    QTabWidget *tabWidget;
    QWidget *tab_2;
    QLabel *label_3;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QSpinBox *y_spin;
    QLabel *label_5;
    QLabel *label_6;
    QSpinBox *z_spin;
    QLabel *label_4;
    QSpinBox *x_spin;
    QPushButton *button_size;
    QSlider *densitySlider;
    QLabel *label_2;
    QWidget *tab;
    QPushButton *pushButton_2;
    QPushButton *button_exsample_2;
    QPushButton *button_exsample_3;
    QPushButton *button_exsample_4;
    QGroupBox *groupBox;
    QTextEdit *main_list;
    QGroupBox *groupBox_2;
    QTextEdit *settings_list;
    QPushButton *clear_button_2;
    QPushButton *clear_button;
    QMenuBar *menuBar;
    QMenu *menuMybar;
    QMenu *menu;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(1250, 1000);
        action = new QAction(MainWindow);
        action->setObjectName("action");
        action_2 = new QAction(MainWindow);
        action_2->setObjectName("action_2");
        action_4 = new QAction(MainWindow);
        action_4->setObjectName("action_4");
        action_5 = new QAction(MainWindow);
        action_5->setObjectName("action_5");
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName("centralWidget");
        draw_label = new QLabel(centralWidget);
        draw_label->setObjectName("draw_label");
        draw_label->setGeometry(QRect(30, 20, 900, 900));
        label = new QLabel(centralWidget);
        label->setObjectName("label");
        label->setGeometry(QRect(950, 90, 67, 17));
        verticalLayoutWidget = new QWidget(centralWidget);
        verticalLayoutWidget->setObjectName("verticalLayoutWidget");
        verticalLayoutWidget->setGeometry(QRect(950, 20, 281, 901));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName("verticalLayout");
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        tabWidget = new QTabWidget(verticalLayoutWidget);
        tabWidget->setObjectName("tabWidget");
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(tabWidget->sizePolicy().hasHeightForWidth());
        tabWidget->setSizePolicy(sizePolicy);
        tabWidget->setMaximumSize(QSize(16777215, 243));
        tab_2 = new QWidget();
        tab_2->setObjectName("tab_2");
        label_3 = new QLabel(tab_2);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(20, 20, 221, 17));
        gridLayoutWidget = new QWidget(tab_2);
        gridLayoutWidget->setObjectName("gridLayoutWidget");
        gridLayoutWidget->setGeometry(QRect(20, 40, 241, 91));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName("gridLayout");
        gridLayout->setContentsMargins(0, 0, 0, 0);
        y_spin = new QSpinBox(gridLayoutWidget);
        y_spin->setObjectName("y_spin");
        y_spin->setMinimum(1);
        y_spin->setMaximum(200);
        y_spin->setSingleStep(5);
        y_spin->setValue(30);

        gridLayout->addWidget(y_spin, 1, 1, 1, 1);

        label_5 = new QLabel(gridLayoutWidget);
        label_5->setObjectName("label_5");

        gridLayout->addWidget(label_5, 0, 1, 1, 1);

        label_6 = new QLabel(gridLayoutWidget);
        label_6->setObjectName("label_6");

        gridLayout->addWidget(label_6, 0, 2, 1, 1);

        z_spin = new QSpinBox(gridLayoutWidget);
        z_spin->setObjectName("z_spin");
        z_spin->setMinimum(1);
        z_spin->setMaximum(200);
        z_spin->setSingleStep(5);
        z_spin->setValue(100);

        gridLayout->addWidget(z_spin, 1, 2, 1, 1);

        label_4 = new QLabel(gridLayoutWidget);
        label_4->setObjectName("label_4");

        gridLayout->addWidget(label_4, 0, 0, 1, 1);

        x_spin = new QSpinBox(gridLayoutWidget);
        x_spin->setObjectName("x_spin");
        x_spin->setMinimum(1);
        x_spin->setMaximum(200);
        x_spin->setSingleStep(5);
        x_spin->setValue(100);

        gridLayout->addWidget(x_spin, 1, 0, 1, 1);

        button_size = new QPushButton(gridLayoutWidget);
        button_size->setObjectName("button_size");

        gridLayout->addWidget(button_size, 2, 0, 1, 3);

        densitySlider = new QSlider(tab_2);
        densitySlider->setObjectName("densitySlider");
        densitySlider->setGeometry(QRect(20, 170, 241, 20));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(densitySlider->sizePolicy().hasHeightForWidth());
        densitySlider->setSizePolicy(sizePolicy1);
        densitySlider->setMaximumSize(QSize(16777215, 16777215));
        QFont font;
        font.setPointSize(11);
        font.setStyleStrategy(QFont::PreferDefault);
        densitySlider->setFont(font);
        densitySlider->setMouseTracking(true);
        densitySlider->setFocusPolicy(Qt::ClickFocus);
        densitySlider->setMinimum(-20);
        densitySlider->setMaximum(20);
        densitySlider->setPageStep(1);
        densitySlider->setSliderPosition(0);
        densitySlider->setTracking(true);
        densitySlider->setOrientation(Qt::Horizontal);
        densitySlider->setInvertedAppearance(false);
        densitySlider->setInvertedControls(false);
        densitySlider->setTickPosition(QSlider::NoTicks);
        densitySlider->setTickInterval(1);
        label_2 = new QLabel(tab_2);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(70, 150, 141, 17));
        tabWidget->addTab(tab_2, QString());
        tab = new QWidget();
        tab->setObjectName("tab");
        pushButton_2 = new QPushButton(tab);
        pushButton_2->setObjectName("pushButton_2");
        pushButton_2->setGeometry(QRect(20, 10, 241, 41));
        button_exsample_2 = new QPushButton(tab);
        button_exsample_2->setObjectName("button_exsample_2");
        button_exsample_2->setGeometry(QRect(20, 60, 241, 41));
        button_exsample_3 = new QPushButton(tab);
        button_exsample_3->setObjectName("button_exsample_3");
        button_exsample_3->setGeometry(QRect(20, 110, 241, 41));
        button_exsample_4 = new QPushButton(tab);
        button_exsample_4->setObjectName("button_exsample_4");
        button_exsample_4->setGeometry(QRect(20, 160, 241, 41));
        tabWidget->addTab(tab, QString());

        verticalLayout->addWidget(tabWidget);

        groupBox = new QGroupBox(verticalLayoutWidget);
        groupBox->setObjectName("groupBox");
        groupBox->setMaximumSize(QSize(16777215, 221));
        main_list = new QTextEdit(groupBox);
        main_list->setObjectName("main_list");
        main_list->setEnabled(true);
        main_list->setGeometry(QRect(0, 20, 279, 200));
        main_list->setMaximumSize(QSize(16777215, 219));
        main_list->setReadOnly(true);

        verticalLayout->addWidget(groupBox);

        groupBox_2 = new QGroupBox(verticalLayoutWidget);
        groupBox_2->setObjectName("groupBox_2");
        groupBox_2->setMaximumSize(QSize(16777215, 221));
        settings_list = new QTextEdit(groupBox_2);
        settings_list->setObjectName("settings_list");
        settings_list->setEnabled(true);
        settings_list->setGeometry(QRect(0, 20, 279, 200));
        settings_list->setMaximumSize(QSize(16777215, 200));
        settings_list->setReadOnly(true);

        verticalLayout->addWidget(groupBox_2);

        clear_button_2 = new QPushButton(verticalLayoutWidget);
        clear_button_2->setObjectName("clear_button_2");
        clear_button_2->setMaximumSize(QSize(16777215, 30));

        verticalLayout->addWidget(clear_button_2);

        clear_button = new QPushButton(verticalLayoutWidget);
        clear_button->setObjectName("clear_button");
        clear_button->setMaximumSize(QSize(16777215, 30));

        verticalLayout->addWidget(clear_button);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName("menuBar");
        menuBar->setGeometry(QRect(0, 0, 1250, 22));
        menuMybar = new QMenu(menuBar);
        menuMybar->setObjectName("menuMybar");
        menu = new QMenu(menuBar);
        menu->setObjectName("menu");
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName("mainToolBar");
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName("statusBar");
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menuMybar->menuAction());
        menuBar->addAction(menu->menuAction());
        menuMybar->addAction(action);
        menuMybar->addAction(action_2);
        menu->addSeparator();
        menu->addAction(action_4);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MyCLoudRender", nullptr));
        action->setText(QCoreApplication::translate("MainWindow", "\320\227\320\260\320\263\321\200\321\203\320\267\320\270\321\202\321\214 \321\204\320\260\320\271\320\273", nullptr));
        action_2->setText(QCoreApplication::translate("MainWindow", "\320\241\320\276\321\205\321\200\320\260\320\275\320\270\321\202\321\214 \320\262 \321\204\320\260\320\271\320\273", nullptr));
        action_4->setText(QCoreApplication::translate("MainWindow", "\320\232\320\276\320\274\320\260\320\275\320\264\321\213", nullptr));
        action_5->setText(QCoreApplication::translate("MainWindow", "\320\236 \320\275\320\260\321\201", nullptr));
        draw_label->setText(QString());
        label->setText(QString());
        label_3->setText(QCoreApplication::translate("MainWindow", "\320\222\320\262\320\265\320\264\320\270\321\202\320\265 \321\200\320\260\320\267\320\274\320\265\321\200\321\213 \320\276\320\261\320\273\320\260\320\272\320\260", nullptr));
        label_5->setText(QCoreApplication::translate("MainWindow", "Ysize:", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "Zsize:", nullptr));
        label_4->setText(QCoreApplication::translate("MainWindow", "Xsize:", nullptr));
        button_size->setText(QCoreApplication::translate("MainWindow", "\320\241\320\263\320\265\320\275\320\265\321\200\320\270\321\200\320\276\320\262\320\260\321\202\321\214", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "\320\237\320\273\320\276\321\202\320\275\320\276\321\201\321\202\321\214 \320\276\320\261\320\273\320\260\320\272\320\276\320\262", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QCoreApplication::translate("MainWindow", "\320\237\320\276\320\273\321\214\320\267\320\276\320\262\320\260\321\202\320\265\320\273\321\214\321\201\320\272\320\270\320\265", nullptr));
        pushButton_2->setText(QCoreApplication::translate("MainWindow", "\320\232\321\200\321\203\320\263\320\273\320\276\320\265 \320\276\320\261\320\273\320\260\320\272\320\276", nullptr));
        button_exsample_2->setText(QCoreApplication::translate("MainWindow", "\320\237\320\273\320\276\321\202\320\275\321\213\320\265 \320\276\320\261\320\273\320\260\320\272\320\260 ", nullptr));
        button_exsample_3->setText(QCoreApplication::translate("MainWindow", "\320\240\320\260\320\267\321\200\320\265\320\266\320\265\320\275\320\275\321\213\320\265 \320\276\320\261\320\273\320\260\320\272\320\260", nullptr));
        button_exsample_4->setText(QCoreApplication::translate("MainWindow", "\320\237\321\200\320\276\320\273\320\265\321\202 \321\207\320\265\321\200\320\265\320\267 \320\276\320\261\320\273\320\260\320\272\320\276", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab), QCoreApplication::translate("MainWindow", "\320\237\321\200\320\270\320\274\320\265\321\200\321\213", nullptr));
        groupBox->setTitle(QCoreApplication::translate("MainWindow", "\320\237\320\260\321\200\320\260\320\274\320\265\321\202\321\200\321\213 \320\276\320\261\320\273\320\260\320\272\320\260", nullptr));
        groupBox_2->setTitle(QCoreApplication::translate("MainWindow", "\320\232\320\276\321\215\321\204\321\204\320\270\321\206\320\270\320\265\320\275\321\202\321\213 \320\277\321\200\320\265\320\276\320\261\321\200\320\260\320\267\320\276\320\262\320\260\320\275\320\270\320\271", nullptr));
        clear_button_2->setText(QCoreApplication::translate("MainWindow", "\320\241\320\261\321\200\320\276\321\201\320\270\321\202\321\214 \320\277\321\200\320\265\320\276\320\261\321\200\320\260\320\267\320\276\320\262\320\260\320\275\320\270\321\217", nullptr));
        clear_button->setText(QCoreApplication::translate("MainWindow", "\320\236\321\207\320\270\321\201\321\202\320\270\321\202\321\214", nullptr));
        menuMybar->setTitle(QCoreApplication::translate("MainWindow", "\320\244\320\260\320\271\320\273", nullptr));
        menu->setTitle(QCoreApplication::translate("MainWindow", "\320\237\320\276\320\274\320\276\321\211\321\214", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
