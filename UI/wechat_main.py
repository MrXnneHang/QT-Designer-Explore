# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\wechat_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Chat_Main(object):
    def setupUi(self, Chat_Main):
        Chat_Main.setObjectName("Chat_Main")
        Chat_Main.resize(770, 483)
        self.verticalLayout = QtWidgets.QVBoxLayout(Chat_Main)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu_wid = QtWidgets.QWidget(Chat_Main)
        self.menu_wid.setMaximumSize(QtCore.QSize(16777215, 50))
        self.menu_wid.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.menu_wid.setObjectName("menu_wid")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.menu_wid)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(550, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.menu_wid)
        self.label.setStyleSheet("font: 12pt \"Arial\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.menu_wid)
        self.pushButton.setMaximumSize(QtCore.QSize(30, 20))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.menu_wid)
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 20))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.menu_wid)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 20))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.menu_wid)
        self.body_wid = QtWidgets.QWidget(Chat_Main)
        self.body_wid.setStyleSheet("background-color: rgb(160,160,160);")
        self.body_wid.setObjectName("body_wid")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.body_wid)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TabWidget = QtWidgets.QTabWidget(self.body_wid)
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_1)
        self.horizontalLayout_2.setContentsMargins(50, 20, 50, 20)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.tab_1)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setContentsMargins(0, 20, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 600))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget_4)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 20)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_5.setMaximumSize(QtCore.QSize(16777215, 450))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.verticalLayout_3.addWidget(self.widget_7)
        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 2)
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.tab_1)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2.addWidget(self.widget_5)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 2)
        self.TabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.message_layout = QtWidgets.QWidget(self.tab_2)
        self.message_layout.setObjectName("message_layout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.message_layout)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.model_select = QtWidgets.QWidget(self.message_layout)
        self.model_select.setObjectName("model_select")
        self.horizontalLayout_6.addWidget(self.model_select)
        self.message_placeholder = QtWidgets.QWidget(self.message_layout)
        self.message_placeholder.setObjectName("message_placeholder")
        self.horizontalLayout_6.addWidget(self.message_placeholder)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 4)
        self.horizontalLayout_3.addWidget(self.message_layout)
        self.widget_3 = QtWidgets.QWidget(self.tab_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 2)
        self.TabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.TabWidget.addTab(self.tab, "")
        self.verticalLayout_2.addWidget(self.TabWidget)
        self.widget = QtWidgets.QWidget(self.body_wid)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 250))
        self.widget.setStyleSheet("background-color: rgb(181, 181, 181);")
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout_2.setStretch(0, 7)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout.addWidget(self.body_wid)
        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(Chat_Main)
        self.TabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Chat_Main)

    def retranslateUi(self, Chat_Main):
        _translate = QtCore.QCoreApplication.translate
        Chat_Main.setWindowTitle(_translate("Chat_Main", "Form"))
        self.label.setText(_translate("Chat_Main", "Title"))
        self.TabWidget.setWhatsThis(_translate("Chat_Main", "<html><head/><body><p>对话一</p></body></html>"))
        self.pushButton_4.setText(_translate("Chat_Main", "开始"))
        self.pushButton_5.setText(_translate("Chat_Main", "PushButton"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_1), _translate("Chat_Main", "开始"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_2), _translate("Chat_Main", "对话一"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab), _translate("Chat_Main", "页"))
