from PyQt5.QtWidgets import QMainWindow,QFileDialog,QVBoxLayout,QHBoxLayout

from UI.chart_selector import Ui_ChartSelector
from Response.util import hidden_layout

class RSP_ChartSelector(QMainWindow,Ui_ChartSelector):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect the CheckBox signal to a slot
        self.line_chart.stateChanged.connect(self.on_checkbox_state_changed)
        self.bar_chart.stateChanged.connect(self.on_checkbox_state_changed)
        self.pie_chart.stateChanged.connect(self.on_checkbox_state_changed)
        # Set initial state of CheckBox
        self.bar_chart.setChecked(True)


    def on_checkbox_state_changed(self, state):
        if state == 0:
            print("CheckBox is unchecked")
        elif state == 2:
            print("CheckBox is checked")