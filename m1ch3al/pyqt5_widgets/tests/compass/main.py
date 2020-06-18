import sys

from PyQt5.QtWidgets import *
from m1ch3al.pyqt5_widgets.compass import Compass


def main():
    app = QApplication(sys.argv)
    compass = Compass()
    compass.set_heading(45)
    compass.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

