from PySide6 import QtCore, QtWidgets
from helpers.events import Events


class MyWidget(QtWidgets.QWidget, Events):
    def __init__(self, category, news):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.initMenu(category)
        self.initTextArea(news)
        

    def initTextArea(self, news):
        self.newsArea = QtWidgets.QLabel()
        news_feed = ""
        for new in news:
            news_feed = f"{news_feed}{new}\n"
        self.newsArea.setText(news_feed)
        self.newsArea.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
        self.layout.addWidget(self.newsArea)


    def initMenu(self, category):
        self.combo = QtWidgets.QComboBox(self)
        self.combo.addItems(category)
        self.layout.addWidget(self.combo)
        self.combo.move(50, 50)
        self.setGeometry(300, 300, 300, 200)
        self.combo.currentTextChanged.connect(self.categoryNews)