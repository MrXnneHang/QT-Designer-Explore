from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, Qt

class ClickQLabel(QLabel):
    """可以被触发的Label,制作动态效果.

    """
    clicked = pyqtSignal() #.clicked.connect()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.background_img = "" # path
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)
