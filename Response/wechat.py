import sys
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QSize, QTimer, QPoint

from modules.bubble_message import MessageType, BubbleMessage,Message_Window
from UI.main import Ui_main
from tools.yml import read_history

class RSP_WeChat(QMainWindow, Ui_main):
    """对话窗口
    @func:
    """
    def __init__(self):
        super(RSP_WeChat, self).__init__()
        self.setupUi(self)


        # 创建 RSP_Wechat 实例
        self.wechat_widget = Message_Window()

        # 将 wechat_widget 添加到 message_placeholder 中
        self.message_layout = QVBoxLayout(self.func1_llm_page)
        self.message_layout.addWidget(self.wechat_widget)
        self.close_button.clicked.connect(self.close)

        self.initialize()

    def initialize(self):
        """初始化数据"""
        self._offset = None
        self._corner_drag = False
        self._right_drag = False
        self._bottom_drag = False
        self.base_system_init()  # 获取边界数值
        
        # 隐藏菜单栏
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 创建阴影效果
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)  # 模糊半径
        shadow.setXOffset(0)  # X方向的偏移
        shadow.setYOffset(0)  # Y方向的偏移
        shadow.setColor(QColor(0, 0, 0, 160))  # 阴影颜色 (黑色，160透明度)

        # 将阴影效果应用到窗口
        self.background.setGraphicsEffect(shadow)

        self.add_history()

    def add_history(self):
        chats = read_history()
        for index, chat in enumerate(chats):
            if chat['name'] == "self":
                bubble_message = BubbleMessage(chat['message'], './data/head2.jpg', Type=MessageType.Text, is_send=True)
                self.wechat_widget.w1.add_message_item(bubble_message)
            else:
                bubble_message = BubbleMessage(chat['message'], './data/head1.jpg', Type=MessageType.Text, is_send=False)
                self.wechat_widget.w1.add_message_item(bubble_message)

    def mousePressEvent(self, event):
        """重写拖拽窗口移动1-点击窗口"""
        if event.button() == Qt.LeftButton and event.pos() in self._corner_rect:
            self._corner_drag = True
            event.accept()
        elif event.button() == Qt.LeftButton and event.pos() in self._right_rect:
            self._right_drag = True
            event.accept()
        elif event.button() == Qt.LeftButton and event.pos() in self._bottom_rect:
            self._bottom_drag = True
            event.accept()
        elif event.button() == Qt.LeftButton:
            self._offset = event.pos()

    def mouseMoveEvent(self, event):
        """重写拖拽窗口移动2-移动窗口"""
        if self._offset:
            new_pos = event.globalPos() - self._offset
            self.move(new_pos)
        elif Qt.LeftButton and self._right_drag:
            self.resize(event.pos().x(), self.height())
            self.resize(event.pos().x(), self.height())
            event.accept()
        elif Qt.LeftButton and self._bottom_drag:
            self.resize(self.width(), event.pos().y())
            self.resize(self.width(), event.pos().y())
            event.accept()
        elif Qt.LeftButton and self._corner_drag:
            self.resize(event.pos().x(), event.pos().y())
            self.resize(event.pos().x(), event.pos().y())
            event.accept()

    def mouseReleaseEvent(self, event):
        """重写拖拽窗口移动3-松开鼠标"""
        if event.button() == Qt.LeftButton:
            self._offset = None
            self._corner_drag = False
            self._bottom_drag = False
            self._right_drag = False
            self.base_system_init()
            self.setCursor(Qt.ArrowCursor)

    def base_system_init(self):
        """获取窗口边界"""
        self._padding = 30
        self._right_rect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1) for y in
                            iter((range(1, self.height() - self._padding)))]
        self._bottom_rect = [QPoint(x, y) for x in range(1, self.width() - self._padding) for y in
                             iter((range(self.height() - self._padding, self.height() + 1)))]
        self._corner_rect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1) for y
                             in iter((range(self.height() - self._padding, self.height() + 1)))]




