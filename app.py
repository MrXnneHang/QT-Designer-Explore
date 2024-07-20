import sys
from PyQt5 import QtWidgets

from Response.path_selector_response import RSP_PathSelector


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = RSP_PathSelector()
    main_window.show()
    sys.exit(app.exec_())