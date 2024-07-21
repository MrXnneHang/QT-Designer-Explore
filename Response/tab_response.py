from PyQt5.QtWidgets import QMainWindow

from UI.tab import Ui_Tab

class RSP_Tab(QMainWindow,Ui_Tab):
    def __init__(self)->None:
        super().__init__()
        self.setupUi(self)
        
    
