from furigana.furigana import get_html

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Thing(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)

        self.webEngineView = QWebEngineView()
        self.loadPage()

        self.textfield = QLineEdit()
        self.textfield.textChanged.connect(lambda: self.webEngineView.setHtml(get_html(self.textfield.text())))
        # self.textfield.textChanged.connect(lambda: print(self.textfield.text()))

        vbox.addWidget(self.textfield)
        vbox.addWidget(self.webEngineView)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('furiganatool')
        self.show()

    def loadPage(self):
            self.webEngineView.setHtml(get_html("ようこそ"))

def main():

    app = QApplication(sys.argv)
    ex = Thing()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()