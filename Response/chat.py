import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtWidgets import QApplication, QDialog, QListWidgetItem, QWidget, QAbstractItemView

# 导入 UI 生成的类
from UI.chat_message import Ui_Chat
from UI.chat_main import Ui_Main

class RSP_Chat(QDialog, Ui_Main):
    def __init__(self):
        super(RSP_Chat, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.self_message_indices = []  # 用于保存你发送的消息的索引
        self.current_message_index = -1  # 当前消息索引

        self.initialize()

    def initialize(self):
        self.add_Chats()
        self.previous_message_button.clicked.connect(self.locate_previous_message)
        self.next_message_button.clicked.connect(self.locate_next_message)

    def add_Chats(self):
        chats = [
            {
                "name": "self",
                "message": "Hi",
                "time": "3:10PM"
            },
            {
                "name": "Maud Carson",
                "message": "Hello",
                "time": "3:10PM"
            },
            {
                "name": "Maud Carson",
                "message": "Hello",
                "time": "3:10PM"
            },
            {
                "name": "Maud Carson",
                "message": "Hello",
                "time": "3:10PM"
            },
            {
                "name": "Maud Carson",
                "message": "How is it today",
                "time": "3:10PM"
            },
            {
                "name": "self",
                "message": "Hi Maud, Are you ok?",
                "time": "4:15PM"
            },
            {
                "name": "Russell Greene",
                "message": "Can you share your opinion?",
                "time": "6:39PM"
            },
            {
                "name": "Cole Strikland",
                "message": "Yes Russell, just don't talk about it with others. Can you share your opinion? I'm waiting for Maud to come back to the chat.",
                "time": "3:25PM",
            },
            {
                "name": "self",
                "message": "I'm waiting for Maud to come back to the chat.",
                "time": "3:26PM",
            },
            {
                "name": "Russell Greene",
                "message": "Can you share your opinion?",
                "time": "6:39PM"
            },
            {
                "name": "Cole Strikland",
                "message": "Yes Russell, just don't talk about it with others. Can you share your opinion? I'm waiting for Maud to come back to the chat.",
                "time": "3:25PM",
            },
            {
                "name": "Russell Greene",
                "message": "Can you share your opinion?",
                "time": "6:39PM"
            },
            {
                "name": "Cole Strikland",
                "message": "Yes Russell, just don't talk about it with others. Can you share your opinion? I'm waiting for Maud to come back to the chat.",
                "time": "3:25PM",
            },
            {
                "name": "Russell Greene",
                "message": "Can you share your opinion?",
                "time": "6:39PM"
            },
            {
                "name": "Cole Strikland",
                "message": "Yes Russell, just don't talk about it with others. Can you share your opinion? I'm waiting for Maud to come back to the chat.",
                "time": "3:25PM",
            },
            {
                "name": "self",
                "message": "I'm waiting for Maud to come back to the chat.",
                "time": "3:26PM",
            },
            {
                "name": "Russell Greene",
                "message": "Can you share your opinion?",
                "time": "6:39PM"
            },
            {
                "name": "Cole Strikland",
                "message": "Yes Russell, just don't talk about it with others. Can you share your opinion? I'm waiting for Maud to come back to the chat.",
                "time": "3:25PM",
            },

        ]
        for index, chat in enumerate(chats):
            widget = QWidget()
            message = Ui_Chat()
            message.setupUi(widget)

            message.name_label.setText(chat['name'])

            message.message_linedit.setText(chat['message'])
            if not chat['time']:
                message.time_label.setStyleSheet("")

            if chat['name'] == "self":
                message.horizontalLayout_2.removeWidget(message.message_right_space_label)
                message.horizontalLayout_2.removeWidget(message.avatar_widget)
                message.name_label.setText('')
                message.message_linedit.setStyleSheet(
                    "color:rgb(120,120,120);background-color: rgb(220, 220, 220);"
                    "border-radius: 12px;border-top-right-radius: 0px;"
                )
                message.message_linedit.setAlignment(Qt.AlignRight)
                message.time_label.setAlignment(Qt.AlignRight)

                # 保存你发送的消息的索引
                self.self_message_indices.append(index)
            else:
                message.horizontalLayout_2.removeWidget(message.message_left_space_label)

            item = QListWidgetItem()
            item.setSizeHint(QSize(50, 80))

            self.listWidget_5.addItem(item)
            self.listWidget_5.setItemWidget(item, widget)
            text_width = QFontMetrics(QFont()).boundingRect(chat['message']).width()
            message.message_linedit.setMaximumWidth(text_width + 50)
            message.message_linedit.setMinimumWidth(text_width + 50)

        # 初始化当前消息索引为最后一条消息
        if self.self_message_indices:
            self.current_message_index = self.self_message_indices[-1]
            self.scroll_to_last_self_message()

    def scroll_to_last_self_message(self):
        if self.self_message_indices:
            last_self_index = self.self_message_indices[-1]
            self.listWidget_5.scrollToItem(self.listWidget_5.item(last_self_index), QAbstractItemView.PositionAtTop)
            self.current_message_index = last_self_index

    def locate_previous_message(self):
        if self.self_message_indices:
            current_pos = self.self_message_indices.index(self.current_message_index) if self.current_message_index in self.self_message_indices else -1
            if current_pos > 0:
                previous_index = self.self_message_indices[current_pos - 1]
                self.listWidget_5.scrollToItem(self.listWidget_5.item(previous_index), QAbstractItemView.PositionAtTop)
                self.current_message_index = previous_index

    def locate_next_message(self):
        if self.self_message_indices:
            current_pos = self.self_message_indices.index(self.current_message_index) if self.current_message_index in self.self_message_indices else -1
            if current_pos < len(self.self_message_indices) - 1:
                next_index = self.self_message_indices[current_pos + 1]
                self.listWidget_5.scrollToItem(self.listWidget_5.item(next_index), QAbstractItemView.PositionAtTop)
                self.current_message_index = next_index