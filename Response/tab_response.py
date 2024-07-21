from PyQt5.QtWidgets import QMainWindow

from UI.tab import Ui_Tab
from Response import util
class RSP_Tab(QMainWindow,Ui_Tab):
    def __init__(self)->None:
        super().__init__()
        self.setupUi(self)
        self.t1_switch_t2.clicked.connect(self.switch_to_tab2)
        self.t2_swicth_t1.clicked.connect(self.switch_to_tab1)
    
    def switch_to_tab1(self):
        util.switch_tab_index(self.TabWidget,1)
    def switch_to_tab2(self):
        util.switch_tab_index(self.TabWidget,2)

    
