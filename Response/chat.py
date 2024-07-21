import random
import sys

from PyQt5.QtCore import Qt, QSize, QTimer, QPoint
from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtWidgets import QApplication, QDialog, QListWidgetItem, QWidget

from UI.chat_message import Ui_Chat
from UI.chat_main import Ui_Main

ICON = [
    "image: url(:/resources/avatar12.png);border-radius: 20px;margin:4px;background-color: rgba(214, 214, 214, 200);",
    "image: url(:/resources/avatar15.png);border-radius: 20px;margin:4px;background-color: rgba(214, 214, 214, 200);",
    "image: url(:/resources/avatar23.png);border-radius: 20px;margin:4px;background-color: rgba(214, 214, 214, 200);",
    "image: url(:/resources/avatar35.png);border-radius: 20px;margin:4px;background-color: rgba(214, 214, 214, 200);",

]


class RSP_Chat(QDialog, Ui_Main):
    def __init__(self):
        super(RSP_Chat, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self._initialization()

    def _initialization(self):
        """初始化数据"""
        self._offset = None
        self._corner_drag = False
        self._right_drag = False
        self._bottom_drag = False
        self.animation_signal = False
        self.animation_time = QTimer()  # 动画计时器
        self.base_system_init()  # 获取边界数值
        self.add_Chats()

    def add_Chats(self):
        chats = [
            {
                "name": "Maud Carson",
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
                "message": "Yes Russell,just dont talk about it with others.Can you share your opinion?I'm waiting for Maud for comeback to the chat.",
                "time": "3:25PM",
            },
            {
                "name": "self",
                "message": "I'm waiting for Maud for comeback to the chat.",
                "time": "3:26PM",
            }
        ]
        for chat in chats:
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
            else:
                message.horizontalLayout_2.removeWidget(message.message_left_space_label)

            item = QListWidgetItem()
            item.setSizeHint(QSize(50, 80))

            self.listWidget_5.addItem(item)
            self.listWidget_5.setItemWidget(item, widget)
            text_width = QFontMetrics(QFont()).boundingRect(chat['message']).width()
            message.message_linedit.setMaximumWidth(text_width + 50)
            message.message_linedit.setMinimumWidth(text_width + 50)


    def base_system_init(self):
        """获取窗口边界"""
        self._padding = 30
        self._right_rect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1) for y in
                            iter((range(1, self.height() - self._padding)))]
        self._bottom_rect = [QPoint(x, y) for x in range(1, self.width() - self._padding) for y in
                             iter((range(self.height() - self._padding, self.height() + 1)))]
        self._corner_rect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1) for y
                             in iter((range(self.height() - self._padding, self.height() + 1)))]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)  # 自适应高分屏
    app.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    main = MyMainForm()
    main.show()
    sys.exit(app.exec_())
