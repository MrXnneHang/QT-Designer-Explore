import re
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtCore import pyqtSignal, QPropertyAnimation, QRect, Qt



class ClickQLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.hover_label_qss = ""
        self.normal_label_qss = ""
        self.initial_geometry = None  # 记录初始几何位置
        self.setAlignment(Qt.AlignCenter)  # 设置文本居中
        self.init_animation()



    def init_animation(self):
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(30)  # 动画持续时间30毫秒

    def enterEvent(self, event):
        if self.initial_geometry is None:
            self.initial_geometry = self.geometry()  # 记录初始几何位置
        self.animate_geometry(scale=1.12)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.animate_geometry(scale=(1))  # 恢复到原始大小
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)

    def animate_geometry(self, scale):
        if self.initial_geometry is None:
            return

        width = self.initial_geometry.width()
        height = self.initial_geometry.height()
        new_width = width * scale
        new_height = height * scale
        new_x = self.initial_geometry.x() - (new_width - width) / 2
        new_y = self.initial_geometry.y() - (new_height - height) / 2
        new_geometry = QRect(new_x, new_y, new_width, new_height)
        
        self.anim.stop()
        self.anim.setStartValue(self.geometry())
        self.anim.setEndValue(new_geometry)
        self.anim.start()

