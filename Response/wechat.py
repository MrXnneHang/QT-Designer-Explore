import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout


from modules.bubble_message import MessageType, BubbleMessage,Message_Window

from UI.wechat_main import Ui_Chat_Main
from tools.yml import read_history
class RSP_WeChat(QDialog, Ui_Chat_Main):
    """对话窗口
    @func:
    """
    def __init__(self):
        super(RSP_WeChat, self).__init__()
        self.setupUi(self)


        # 创建 RSP_Wechat 实例
        self.wechat_widget = Message_Window()

        # 将 wechat_widget 添加到 message_placeholder 中
        self.message_layout = QVBoxLayout(self.message_placeholder)
        self.message_layout.addWidget(self.wechat_widget)

        self.initialize()

    def initialize(self):
        self.add_history()

    def add_history(self):
        chats = read_history()
        for index, chat in enumerate(chats):
            if chat['name'] == "self":
                bubble_message = BubbleMessage(chat['message'], './data/head1.svg', Type=MessageType.Text, is_send=True)
                self.wechat_widget.w1.add_message_item(bubble_message)
            else:
                bubble_message = BubbleMessage(chat['message'], './data/head1.jpg', Type=MessageType.Text, is_send=False)
                self.wechat_widget.w1.add_message_item(bubble_message)


