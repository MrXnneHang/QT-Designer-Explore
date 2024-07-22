
from datetime import datetime
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QApplication

from modules.bubble_message import BubbleMessage, ChatWidget,MessageType,Notice



class Wechat_Message(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.resize(500, 600)
        self.w1 = ChatWidget()
        # 获取当前日期和时间
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
        # 创建 Notice 对象
        time_message = Notice(current_time)
        self.w1.add_message_item(time_message)
        w2 = QLabel("你需要文件1文件2")
        layout.addWidget(self.w1)
        layout.addWidget(w2)
        self.setLayout(layout)

    def value(self, val):
        print('pos:', val)
        print('滚动条最大值', self.w1.verticalScrollBar().maximum())


