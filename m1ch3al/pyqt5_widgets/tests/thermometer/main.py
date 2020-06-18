import sys

from PyQt5.QtWidgets import *
from m1ch3al.pyqt5_widgets.tests.thermometer.test_gui import TestGui


def main():
    app = QApplication(sys.argv)
    main_test_gui = TestGui()
    main_test_gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

