import sys
import random

from UI import Ui_MainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False
        self.painter = QPainter()


    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            self.color = QColor(random.randrange(256), random.randrange(256), random.randrange(256))
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