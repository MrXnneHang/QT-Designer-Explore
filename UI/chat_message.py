# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\chat_message.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Chat(object):
    def setupUi(self, Chat):
        Chat.setObjectName("Chat")
        Chat.resize(518, 81)
        self.verticalLayout = QtWidgets.QVBoxLayout(Chat)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Chat)
        self.frame.setStyleSheet("font-family:\"微软雅黑\";\n"
"background-color: rgb(251, 246, 252);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.avatar_widget = QtWidgets.QWidget(self.frame)
        self.avatar_widget.setMinimumSize(QtCore.QSize(30, 30))
        self.avatar_widget.setMaximumSize(QtCore.QSize(30, 30))
        self.avatar_widget.setStyleSheet("image: url(:/resources/avatar12.png);\n"
"border-radius: 11px;\n"
"margin:4px;\n"
"background-color: rgba(214, 214, 214, 200);")
        self.avatar_widget.setObjectName("avatar_widget")
        self.horizontalLayout.addWidget(self.avatar_widget)
        self.name_label = QtWidgets.QLabel(self.frame)
        self.name_label.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.name_label.setObjectName("name_label")
        self.horizontalLayout.addWidget(self.name_label)
        self.user_right_space_label = QtWidgets.QLabel(self.frame)
        self.user_right_space_label.setText("")
        self.user_right_space_label.setObjectName("user_right_space_label")
        self.horizontalLayout.addWidget(self.user_right_space_label)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 9)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.frame)
        self.widget_3.setMinimumSize(QtCore.QSize(30, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(30, 9999))
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.message_left_space_label = QtWidgets.QLabel(self.frame)
        self.message_left_space_label.setText("")
        self.message_left_space_label.setObjectName("message_left_space_label")
        self.horizontalLayout_2.addWidget(self.message_left_space_label)
        self.message_linedit = QtWidgets.QLineEdit(self.frame)
        self.message_linedit.setMinimumSize(QtCore.QSize(0, 32))
        self.message_linedit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.message_linedit.setStyleSheet("background-color: rgb(243, 134, 166);\n"
"border-radius: 12px;\n"
"border-top-left-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left:12px;\n"
"\n"
"\n"
"")
        self.message_linedit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.message_linedit.setReadOnly(True)
        self.message_linedit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.message_linedit.setObjectName("message_linedit")
        self.horizontalLayout_2.addWidget(self.message_linedit)
        self.message_right_space_label = QtWidgets.QLabel(self.frame)
        self.message_right_space_label.setText("")
        self.message_right_space_label.setObjectName("message_right_space_label")
        self.horizontalLayout_2.addWidget(self.message_right_space_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.frame)
        self.widget_4.setMinimumSize(QtCore.QSize(48, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(48, 9999))
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.time_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(6)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color: rgb(148, 148, 148);")
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_3.addWidget(self.time_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Chat)
        QtCore.QMetaObject.connectSlotsByName(Chat)

    def retranslateUi(self, Chat):
        _translate = QtCore.QCoreApplication.translate
        Chat.setWindowTitle(_translate("Chat", "Form"))
        self.name_label.setText(_translate("Chat", "Maud Carson"))
        self.message_linedit.setText(_translate("Chat", "dfefe"))
        self.time_label.setText(_translate("Chat", "3:10PM"))