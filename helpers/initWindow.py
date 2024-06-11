import sys
from PySide6 import QtWidgets
from lib.MyWidget import MyWidget

class InitWindow:
    def __init__(self, data) -> None:
        app = QtWidgets.QApplication([])
        widget = MyWidget(data)
        widget.resize(800, 600)
        widget.show()
        sys.exit(app.exec())