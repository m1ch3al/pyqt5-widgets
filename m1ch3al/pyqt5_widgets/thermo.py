from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class _InnerThermometer(QWidget):
    def __init__(self, min_value, max_value, steps, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_value = min_value
        self.max_value = max_value
        self.steps = steps
        self.setSizePolicy(
            QSizePolicy.MinimumExpanding,
            QSizePolicy.MinimumExpanding
        )
        self._white = QtGui.QColor('white')
        self._black = QtGui.QColor('black')
        self._orange = QtGui.QColor('orange')

        self._left_padding = 70
        self._upper_padding = 10
        self._lower_padding = None
        self._lower_padding_offset = -10
        self._thermo_width_external = 20
        painter = QtGui.QPainter(self)
        self._lower_padding = painter.device().height() + self._lower_padding_offset
        self._thermo_rect = None
        self._value_to_draw = None

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        self._lower_padding = painter.device().height() + self._lower_padding_offset
        painter.end()
        self._draw_scale(e)
        self._draw_thermo(e)
        self._draw_value(e)

    def _draw_value(self, event):
        if self._value_to_draw is None:
            return
        else:
            thermo_height = self._thermo_rect.height()
            one_pixels_step = float(thermo_height) / self.steps
            if self.min_value >= 0:
                value_to_pixel = abs(self.min_value - self._value_to_draw) * one_pixels_step
            else:
                if self._value_to_draw < 0:
                    value_to_pixel = (abs(self.min_value) - abs(self._value_to_draw)) * one_pixels_step
                else:
                    value_to_pixel = (abs(self.min_value) + self._value_to_draw) * one_pixels_step

            print("{}       {}".format(self._value_to_draw, value_to_pixel))
            painter = QtGui.QPainter(self)
            brush = QtGui.QBrush()
            brush.setColor(self._orange)
            brush.setStyle(Qt.SolidPattern)
            rect = QtCore.QRect(self._thermo_rect.bottomLeft().x(), self._thermo_rect.bottomLeft().y()+1,
                                self._thermo_width_external - 4, -value_to_pixel)
            painter.fillRect(rect, brush)
            painter.end()

    def _draw_scale(self, event):
        painter = QtGui.QPainter(self)

        brush = QtGui.QBrush()
        brush.setColor(self._black)
        brush.setStyle(Qt.SolidPattern)

        # Draw vertical line
        line = QtCore.QLine(self._left_padding-14, self._upper_padding, self._left_padding-14, self._lower_padding)
        painter.drawLine(line)

        # Draw end with label
        line = QtCore.QLine(self._left_padding - 30, self._upper_padding, self._left_padding - 14, self._upper_padding)
        painter.drawLine(line)
        rect = QtCore.QRect(self._left_padding - 70, self._upper_padding-8, self._left_padding - 35,
                            self._upper_padding + 5)
        painter.drawText(rect, Qt.AlignRight, "{}".format(self.max_value))

        # Draw start with label
        line = QtCore.QLine(self._left_padding - 30,  self._lower_padding, self._left_padding - 14, self._lower_padding)
        painter.drawLine(line)
        rect = QtCore.QRect(self._left_padding - 70, self._lower_padding-8, self._left_padding - 35,
                            self._lower_padding)
        painter.drawText(rect, Qt.AlignRight, "{}".format(self.min_value))

        step_length = int((self._lower_padding - self._upper_padding) / self.steps)
        step_length_value = round(((self.max_value - self.min_value) / self.steps), 1)

        horizontal_x = self._upper_padding + step_length
        current_value = self.max_value - step_length_value
        for i in range(0, self.steps-1):
            line = QtCore.QLine(self._left_padding - 30, horizontal_x, self._left_padding - 14,
                                horizontal_x)
            painter.drawLine(line)
            rect = QtCore.QRect(self._left_padding - 70, horizontal_x - 8, self._left_padding - 35,
                                self._lower_padding)
            painter.drawText(rect, Qt.AlignRight, "{}".format(round(current_value, 2)))
            horizontal_x += step_length
            current_value -= step_length_value
        painter.end()

    def _draw_thermo(self, event):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        brush.setColor(self._black)
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(self._left_padding, self._upper_padding, self._thermo_width_external,
                            self._lower_padding + self._lower_padding_offset)
        painter.fillRect(rect, brush)

        brush.setColor(QtGui.QColor(229, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        self._thermo_rect = QtCore.QRect(self._left_padding + 2, self._upper_padding + 2,
                                         self._thermo_width_external - 4,
                                         self._lower_padding + self._lower_padding_offset - 4)
        painter.fillRect(self._thermo_rect, brush)
        painter.end()

    def set_value(self, value):
        self._value_to_draw = value


class Thermometer(QWidget):
    def __init__(self, min_value, max_value, steps):
        super().__init__()
        layout = QVBoxLayout()
        self._min_value = min_value
        self._max_value = max_value
        self._steps = steps
        self._thermo = _InnerThermometer(min_value, max_value, steps)
        layout.addWidget(self._thermo)
        self.setLayout(layout)

    def set_min_value(self, new_min_value):
        self._min_value = new_min_value
        self._thermo.min_value = self._min_value
        self._thermo.update()

    def set_max_value(self, new_max_value):
        self._max_value = new_max_value
        self._thermo.max_value = self._max_value
        self._thermo.update()

    def set_steps(self, new_steps_value):
        self._steps = new_steps_value
        self._thermo.steps = self._steps
        self._thermo.update()

    def set_value(self, value):
        if value <= self._min_value:
            self._thermo.set_value(self._min_value)
            self._thermo.update()
            return
        if value >= self._max_value:
            self._thermo.set_value(self._max_value)
            self._thermo.update()
            return
        self._thermo.set_value(value)
        self._thermo.update()

