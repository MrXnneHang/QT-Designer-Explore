import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from Response.path_selector_response import RSP_PathSelector
from Response.chart_selector_response import RSP_ChartSelector
from Response.tab_response import RSP_Tab
from Response.click_label_response import RSP_ClickLabel
from Response.chat import RSP_Chat

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #app.setAttribute(Qt.AA_EnableHighDpiScaling, True)  # 自适应高分屏
    #app.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    # # Path Selector
    # main_window = RSP_PathSelector()
    # main_window.hidden_Above()
    # main_window.show()

    # # Chart Seletor
    # main_window = RSP_ChartSelector()
    # main_window.show()

    # # Tab
    # main_window = RSP_Tab()
    # main_window.show()

    # # ClickLabel
    # main_window = RSP_ClickLabel()
    # main_window.show()

    # Chat
    main_window = RSP_Chat()
    main_window.show()
    
    sys.exit(app.exec_())