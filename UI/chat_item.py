# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Item(object):
    def setupUi(self, Item):
        if not Item.objectName():
            Item.setObjectName(u"Item")
        Item.resize(171, 42)
        self.horizontalLayout = QHBoxLayout(Item)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Item)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"font-family:\"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"background-color: rgb(251, 246, 252);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(30, 30))
        self.widget_2.setMaximumSize(QSize(30, 30))
        self.widget_2.setStyleSheet(u"image: url(:/resources/avatar12.png);\n"
"border-radius: 11px;\n"
"margin:4px;\n"
"background-color: rgba(214, 214, 214, 200);")

        self.horizontalLayout_2.addWidget(self.widget_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: 87 8pt \"Arial Black\";")

        self.verticalLayout.addWidget(self.label_2)

        self.form = QLabel(self.widget)
        self.form.setObjectName(u"form")
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(6)
        self.form.setFont(font1)
        self.form.setStyleSheet(u"color: rgb(148, 148, 148);")

        self.verticalLayout.addWidget(self.form)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(15, 15))
        self.widget_3.setMaximumSize(QSize(15, 15))
        self.widget_3.setStyleSheet(u"image: url(:/resources/\u6709\u6d88\u606f.png);")

        self.horizontalLayout_2.addWidget(self.widget_3)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Item)

        QMetaObject.connectSlotsByName(Item)
    # setupUi

    def retranslateUi(self, Item):
        Item.setWindowTitle(QCoreApplication.translate("Item", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Item", u"Groups", None))
        self.form.setText(QCoreApplication.translate("Item", u"Okay, Nice work", None))
    # retranslateUi

