from PyQt5.QtWidgets import QMainWindow,QFileDialog

from UI.path_selector import Ui_PathSelector
from Response import util 

class RSP_PathSelector(QMainWindow,Ui_PathSelector):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.path = ""
        self.path_selector_1.clicked.connect(lambda:self.open_file_dialog(self.path_line_1))
        self.path_selector_2.clicked.connect(lambda:self.open_file_dialog(self.path_line_2))
        self.path_selector_3.clicked.connect(lambda:self.open_file_dialog(self.path_line_3))
        self.path_selector_4.clicked.connect(lambda:self.open_file_dialog(self.path_line_4))
    
    def hidden_Above(self):
        util.hidden_layout(self.Path_Selector_Above)
    
    def hidden_Below(self):
        util.hidden_layout(self.Path_Selector_Below)

    def open_file_dialog(self,line_edit):
        # 弹出文件对话框
        path = QFileDialog.getOpenFileName(self, "选择文件位置", "")
        if path:
            # path-like:('D:/program/Designer/README.md', 'All Files (*)')
            line_edit.setText(path[0])  # 将选择的路径设置到LineEdit中

            # print(f"{self.path_line_1.text()}\n"
            #       f"{self.path_line_2.text()}\n"
            #       f"{self.path_line_3.text()}\n"
            #       f"{self.path_line_4.text()}\n")


