from PyQt5.Qt import *
from PyQt5.QtGui import QPixmap
from m1ch3al.pyqt5_widgets.tests.thermometer.test_gui_ui import Ui_TestGui
from m1ch3al.pyqt5_widgets.thermo import Thermometer


class TestGui(QMainWindow, Ui_TestGui):
    def __init__(self):
        super(TestGui, self).__init__()
        self.setupUi(self)
        self._initialize_event()

    def _initialize_event(self):
        self.pushButton_exit.clicked.connect(close_application)
        self.pushButton_send.clicked.connect(self.send_data)

        self.thermo_widget = Thermometer(0, 100, 10)
        thermo_layout = QVBoxLayout()
        thermo_layout.addWidget(self.thermo_widget)
        self.frame_thermo.setLayout(thermo_layout)
        self.lineEdit.setText("40")

    def send_data(self):
        value = float(self.lineEdit.text())
        self.thermo_widget.set_value(value)


def close_application():
    exit(0)
