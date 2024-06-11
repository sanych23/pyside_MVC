# import sys
# from PySide6 import QtWidgets
# from lib.MyWidget import MyWidget
from helpers.initWindow import InitWindow
from model import FormMain


class Controller:
    

    def mainAction(self) -> None:

        model = FormMain()
        InitWindow(model.getAllData())   




    def defaultAction(self) -> None:
        pass

c = Controller()
c.mainAction()

