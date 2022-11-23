import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from random import randrange


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.k = 0
        self.pushButton.clicked.connect(self.run)
        self.pixmap = QPixmap('Желтый шарик.png')

    def run(self):
        self.k = randrange(100)
        self.label.move(randrange(500), randrange(500))
        self.label.resize(200, 200)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())