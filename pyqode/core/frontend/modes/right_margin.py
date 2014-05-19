# -*- coding: utf-8 -*-
"""
This module contains the right margin mode.
"""
from pyqode.core import settings, style
from pyqode.core.frontend import Mode, mark_whole_doc_dirty
from pyqode.qt import QtWidgets, QtGui


class RightMarginMode(Mode):
    """
    Display a right margin at column 80 by default.

    """
    @property
    def color(self):
        """
        Gets/sets the color of the margin
        """
        return self._color

    @color.setter
    def color(self, value):
        """
        Gets/sets the color of the margin
        """
        self._color = value
        self._pen = QtGui.QPen(self._color)
        mark_whole_doc_dirty(self.editor)
        self.editor.repaint()

    @property
    def position(self):
        """
        Gets/sets the position of the margin
        """
        return self._margin_pos

    @position.setter
    def position(self, value):
        """
        Gets/sets the position of the margin
        """
        self._margin_pos = value

    def __init__(self):
        Mode.__init__(self)
        self._margin_pos = 79
        self._margin_pos = settings.right_margin_pos
        self._color = style.right_margin_color
        self._pen = QtGui.QPen(self._color)

    def refresh_settings(self):
        self._margin_pos = settings.right_margin_pos
        self.editor.repaint()

    def refresh_style(self):
        self._color = style.right_margin_color
        self._pen = QtGui.QPen(self._color)
        self._pen = QtGui.QPen(self._color)
        mark_whole_doc_dirty(self.editor)
        self.editor.repaint()

    def _on_state_changed(self, state):
        """
        Connects/Disconnects to the painted event of the editor

        :param state: Enable state
        """
        if state:
            self.editor.painted.connect(self._paint_margin)
            self.editor.repaint()
        else:
            self.editor.painted.disconnect(self._paint_margin)
            self.editor.repaint()

    def _paint_margin(self, event):  # pylint: disable=unused-argument
        """ Paints the right margin after editor paint event. """
        font = self.editor.currentCharFormat().font()
        metrics = QtGui.QFontMetricsF(font)
        pos = self._margin_pos
        offset = self.editor.contentOffset().x() + \
            self.editor.document().documentMargin()
        x80 = round(metrics.width(' ') * pos) + offset
        painter = QtGui.QPainter(self.editor.viewport())
        painter.setPen(self._pen)
        painter.drawLine(x80, 0, x80, 2 ** 16)
