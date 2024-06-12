from helpers.initWindow import InitWindow
from model import FormCategory


class Controller:
    
    def mainAction(self) -> None:
        model = FormCategory()
        InitWindow(model.getAllCategory(), model.getAllNews())   

    def defaultAction(self) -> None:
        pass


c = Controller()
c.mainAction()

