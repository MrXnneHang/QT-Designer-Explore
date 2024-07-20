import sys
from PyQt5 import QtWidgets

from Response.path_selector_response import RSP_PathSelector
from Response.chart_selector_response import RSP_ChartSelector


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # # Path Selector
    # main_window = RSP_PathSelector()
    # main_window.hidden_Above()
    # main_window.show()

    # Chart Seletor
    main_window = RSP_ChartSelector()
    main_window.show()

    
    sys.exit(app.exec_())