# import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
# from controller import Controller


class MyWidget(QtWidgets.QWidget):
    def __init__(self, data):
        super().__init__()

        self.hello = data

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)


        combo = QtWidgets.QComboBox(self)
        combo.addItems(["Январь", "Февраль",
                        "Март", "Апрель", "Май"])
 
        combo.move(50, 50)
 
        self.setGeometry(300, 300, 300, 200)
        # self.setWindowTitle('QComboBox')
        # self.show()



    @QtCore.Slot()
    def magic(self):
        data = random.choice(self.hello)
        msg = f"{data["msg"]} - {data["name"]}"
        self.text.setText(msg)

# Controller.mainAction()
