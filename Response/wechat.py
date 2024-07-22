import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout

from modules.wechat_message import Wechat_Message
from modules.bubble_message import MessageType, BubbleMessage

from UI.wechat_main import Ui_Chat_Main
from tools.yml import read_history
class RSP_WeChat(QDialog, Ui_Chat_Main):
    """对话窗口
    @func:
    locate_previous_message: 定位上一条自己发的消息
    locate_next_message: 定位下一条自己发的消息
    scroll_to_last_self_message: 根据定位的index将自己的消息置于顶部。
    """
    def __init__(self):
        super(RSP_WeChat, self).__init__()
        self.setupUi(self)

        self.self_message_indices = []  # 用于保存你发送的消息的索引
        self.current_message_index = -1  # 当前消息索引

        # 创建 RSP_Wechat 实例
        self.wechat_widget = Wechat_Message()

        # 将 wechat_widget 添加到 message_placeholder 中
        self.message_layout = QVBoxLayout(self.message_placeholder)
        self.message_layout.addWidget(self.wechat_widget)

        self.initialize()

    def initialize(self):
        self.add_Chats()

    def add_Chats(self):
        chats = read_history()
        for index, chat in enumerate(chats):
            if chat['name'] == "self":
                bubble_message = BubbleMessage(chat['message'], './data/head1.svg', Type=MessageType.Text, is_send=True)
                self.wechat_widget.w1.add_message_item(bubble_message)
                self.self_message_indices.append(index)
            else:
                bubble_message = BubbleMessage(chat['message'], './data/head1.jpg', Type=MessageType.Text, is_send=False)
                self.wechat_widget.w1.add_message_item(bubble_message)



