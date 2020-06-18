from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class _InnerCompass(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setSizePolicy(
            QSizePolicy.MinimumExpanding,
            QSizePolicy.MinimumExpanding
        )
        self._white = QtGui.QColor('white')
        self._black = QtGui.QColor('black')
        self._orange = QtGui.QColor('orange')

        self._angle = 0.0
        self._margins = 10
        self._pointText = {0: "N", 45: "NE", 90: "E", 135: "SE", 180: "S", 225: "SW", 270: "W", 315: "NW"}

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        #painter.fillRect(event.rect(), self.palette().brush(QPalette.Window))
        painter.fillRect(event.rect(), self.palette().brush(QPalette.Window))
        self.drawMarkings(painter)
        self.drawNeedle(painter)
        painter.end()

    def drawMarkings(self, painter):
        painter.save()
        painter.translate(self.width() / 2, self.height() / 2)
        scale = min((self.width() - self._margins) / 120.0, (self.height() - self._margins) / 120.0)
        painter.scale(scale, scale)
        font = QFont(self.font())
        font.setPixelSize(10)
        metrics = QFontMetricsF(font)
        painter.setFont(font)
        painter.setBrush(QBrush(Qt.black))
        #painter.setPen(self.palette().color(QPalette.Shadow))
        i = 0
        while i < 360:
            if i % 45 == 0:
                painter.drawLine(0, -40, 0, -50)
                painter.drawText(-metrics.width(self._pointText[i]) / 2.0, -52, self._pointText[i])
            else:
                painter.drawLine(0, -45, 0, -50)
            painter.rotate(15)
            i += 15
        painter.restore()

    def drawNeedle(self, painter):
        painter.save()
        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(self._angle)
        scale = min((self.width() - self._margins) / 120.0, (self.height() - self._margins) / 120.0)
        painter.scale(scale, scale)
        painter.setPen(QPen(Qt.NoPen))

        painter.setBrush(QBrush(Qt.darkGray))
        painter.drawPolygon(QPolygon([QPoint(-10, 0), QPoint(0, -45), QPoint(10, 0), QPoint(0, 35), QPoint(-10, 0)]))
        #painter.setBrush(self.palette().brush(QPalette.Highlight))
        painter.setBrush(QBrush(Qt.red))
        painter.drawPolygon(QPolygon([QPoint(-5, -25), QPoint(0, -55), QPoint(5, -25), QPoint(0, -30), QPoint(-5, -25)]))

        #self.setPalette(QPalette(Qt.green))
        painter.restore()

    def sizeHint(self):
        return QSize(150, 150)

    def set_heading(self, heading):
        self._angle = heading


class Compass(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self._compass = _InnerCompass()
        layout.addWidget(self._compass)
        self.setLayout(layout)

    def set_heading(self, heading_value):
        self._compass.set_heading(heading_value)
        self._compass.repaint()

