# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'path_selector.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PathSelector(object):
    def setupUi(self, PathSelector):
        PathSelector.setObjectName("PathSelector")
        PathSelector.resize(1026, 577)
        self.centralwidget = QtWidgets.QWidget(PathSelector)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 460, 891, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Path_Selector_1 = QtWidgets.QHBoxLayout()
        self.Path_Selector_1.setObjectName("Path_Selector_1")
        self.path_select_reminder_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.path_select_reminder_4.setStyleSheet("")
        self.path_select_reminder_4.setObjectName("path_select_reminder_4")
        self.Path_Selector_1.addWidget(self.path_select_reminder_4)
        self.path_line_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.path_line_3.setObjectName("path_line_3")
        self.Path_Selector_1.addWidget(self.path_line_3)
        self.path_selector_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.path_selector_3.setEnabled(True)
        self.path_selector_3.setText("")
        self.path_selector_3.setAutoRepeatDelay(300)
        self.path_selector_3.setObjectName("path_selector_3")
        self.Path_Selector_1.addWidget(self.path_selector_3)
        self.horizontalLayout_2.addLayout(self.Path_Selector_1)
        self.Path_Selector_2 = QtWidgets.QHBoxLayout()
        self.Path_Selector_2.setObjectName("Path_Selector_2")
        self.path_select_reminder_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.path_select_reminder_5.setStyleSheet("")
        self.path_select_reminder_5.setObjectName("path_select_reminder_5")
        self.Path_Selector_2.addWidget(self.path_select_reminder_5)
        self.path_line_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.path_line_4.setObjectName("path_line_4")
        self.Path_Selector_2.addWidget(self.path_line_4)
        self.path_selector_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.path_selector_4.setEnabled(True)
        self.path_selector_4.setText("")
        self.path_selector_4.setAutoRepeatDelay(300)
        self.path_selector_4.setObjectName("path_selector_4")
        self.Path_Selector_2.addWidget(self.path_selector_4)
        self.horizontalLayout_2.addLayout(self.Path_Selector_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Path_Selector_3 = QtWidgets.QHBoxLayout()
        self.Path_Selector_3.setObjectName("Path_Selector_3")
        self.path_select_reminder_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.path_select_reminder_2.setStyleSheet("")
        self.path_select_reminder_2.setObjectName("path_select_reminder_2")
        self.Path_Selector_3.addWidget(self.path_select_reminder_2)
        self.path_line_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.path_line_1.setObjectName("path_line_1")
        self.Path_Selector_3.addWidget(self.path_line_1)
        self.path_selector_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.path_selector_1.setEnabled(True)
        self.path_selector_1.setText("")
        self.path_selector_1.setAutoRepeatDelay(300)
        self.path_selector_1.setObjectName("path_selector_1")
        self.Path_Selector_3.addWidget(self.path_selector_1)
        self.horizontalLayout.addLayout(self.Path_Selector_3)
        self.Path_Selector_4 = QtWidgets.QHBoxLayout()
        self.Path_Selector_4.setObjectName("Path_Selector_4")
        self.path_select_reminder_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.path_select_reminder_3.setStyleSheet("")
        self.path_select_reminder_3.setObjectName("path_select_reminder_3")
        self.Path_Selector_4.addWidget(self.path_select_reminder_3)
        self.path_line_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.path_line_2.setObjectName("path_line_2")
        self.Path_Selector_4.addWidget(self.path_line_2)
        self.path_selector_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.path_selector_2.setEnabled(True)
        self.path_selector_2.setText("")
        self.path_selector_2.setAutoRepeatDelay(300)
        self.path_selector_2.setObjectName("path_selector_2")
        self.Path_Selector_4.addWidget(self.path_selector_2)
        self.horizontalLayout.addLayout(self.Path_Selector_4)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        PathSelector.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PathSelector)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1026, 23))
        self.menubar.setObjectName("menubar")
        PathSelector.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PathSelector)
        self.statusbar.setObjectName("statusbar")
        PathSelector.setStatusBar(self.statusbar)

        self.retranslateUi(PathSelector)
        QtCore.QMetaObject.connectSlotsByName(PathSelector)

    def retranslateUi(self, PathSelector):
        _translate = QtCore.QCoreApplication.translate
        PathSelector.setWindowTitle(_translate("PathSelector", "MainWindow"))
        self.path_select_reminder_4.setText(_translate("PathSelector", "选择路径:"))
        self.path_select_reminder_5.setText(_translate("PathSelector", "选择路径:"))
        self.path_select_reminder_2.setText(_translate("PathSelector", "选择路径:"))
        self.path_select_reminder_3.setText(_translate("PathSelector", "选择路径:"))