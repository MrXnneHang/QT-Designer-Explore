# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tab(object):
    def setupUi(self, Tab):
        Tab.setObjectName("Tab")
        Tab.resize(1070, 577)
        self.centralwidget = QtWidgets.QWidget(Tab)
        self.centralwidget.setObjectName("centralwidget")
        self.TabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.TabWidget.setGeometry(QtCore.QRect(0, 0, 851, 391))
        self.TabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border-top: 2px solid rgba(0, 0, 0, 1); /* 黑色 */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-size: 12px;\n"
"    font-weight: 500;\n"
"    padding: 10px 25px; /* 增加内边距 */\n"
"    border-bottom: none;\n"
"    min-width: 45px;\n"
"   \n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    color: rgba(123,190,254, 1); /* 淡蓝色 */\n"
"    border-bottom: 2px solid rgba(123,190,254, 1); /* 淡蓝色 */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-bottom: 2px;\n"
"}\n"
"")
        self.TabWidget.setObjectName("TabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.t1_label_1 = QtWidgets.QLabel(self.tab_1)
        self.t1_label_1.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.t1_label_1.setStyleSheet("font-family: \"Microsoft YaHei\";")
        self.t1_label_1.setObjectName("t1_label_1")
        self.t1_switch_t2_button = QtWidgets.QPushButton(self.tab_1)
        self.t1_switch_t2_button.setGeometry(QtCore.QRect(10, 90, 281, 141))
        self.t1_switch_t2_button.setStyleSheet("font-family: \"Microsoft YaHei\";")
        self.t1_switch_t2_button.setObjectName("t1_switch_t2_button")
        self.TabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.t2_label_2 = QtWidgets.QLabel(self.tab_2)
        self.t2_label_2.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.t2_label_2.setStyleSheet("font-family: \"Microsoft YaHei\";")
        self.t2_label_2.setObjectName("t2_label_2")
        self.t2_swicth_t1_button = QtWidgets.QPushButton(self.tab_2)
        self.t2_swicth_t1_button.setGeometry(QtCore.QRect(110, 90, 281, 141))
        self.t2_swicth_t1_button.setStyleSheet("font-family: \"Microsoft YaHei\";")
        self.t2_swicth_t1_button.setObjectName("t2_swicth_t1_button")
        self.TabWidget.addTab(self.tab_2, "")
        Tab.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tab)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1070, 23))
        self.menubar.setObjectName("menubar")
        Tab.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tab)
        self.statusbar.setObjectName("statusbar")
        Tab.setStatusBar(self.statusbar)

        self.retranslateUi(Tab)
        self.TabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Tab)

    def retranslateUi(self, Tab):
        _translate = QtCore.QCoreApplication.translate
        Tab.setWindowTitle(_translate("Tab", "MainWindow"))
        self.t1_label_1.setText(_translate("Tab", "这里是tab1"))
        self.t1_switch_t2_button.setText(_translate("Tab", "Switch To Tab 2"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_1), _translate("Tab", "Tab 1"))
        self.t2_label_2.setText(_translate("Tab", "这里是tab2"))
        self.t2_swicth_t1_button.setText(_translate("Tab", "Switch To Tab 1"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_2), _translate("Tab", "Tab 2"))
