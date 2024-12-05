import sys
import random

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.paint)
        self.color = QColor(255, 255, 0)
        self.do_paint = False
        self.painter = QPainter()


    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            self.rad = random.randrange(1000)
            self.painter = QPainter()
            self.painter.begin(self)
            self.painter.setBrush(self.color)
            self.painter.setPen(self.color)
            self.painter.drawEllipse(0, 0, self.rad, self.rad)
            self.painter.end()
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())