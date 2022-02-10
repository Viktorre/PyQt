import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def main():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(100, 100, 200, 50)
    b.move(50, 20)
    w.setmainTitle("PyQt5")
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    #https://www.tutorialspoint.com/pyqt5/pyqt5_hello_world.htm