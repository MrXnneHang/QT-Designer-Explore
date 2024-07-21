from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from UI.click_label import Ui_ClickLabel
from Response import util

class RSP_ClickLabel(QMainWindow,Ui_ClickLabel):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.t1_switch_t2_label.clicked.connect(self.switch_to_tab2)
        self.t2_switch_t1_label.clicked.connect(self.switch_to_tab1)
    
    def switch_to_tab2(self):
        # print("Switching to Tab 2")
        util.switch_tab_index(self.TabWidget,2)
    
    def switch_to_tab1(self):
        # print("Switching to Tab 1")
        util.switch_tab_index(self.TabWidget,1)
