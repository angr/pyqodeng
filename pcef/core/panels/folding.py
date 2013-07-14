#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PCEF - Python/Qt Code Editing Framework
# Copyright 2013, Colin Duquesnoy <colin.duquesnoy@gmail.com>
#
# This software is released under the LGPLv3 license.
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
"""
This module contains the marker panel
"""
from pcef.qt import QtCore, QtGui
from pcef.core import constants
from pcef.core.panel import Panel
from pcef.core.decoration import TextDecoration
from pcef.core.system import mergedColors, driftColor


class FoldingIndicator(object):
    UNFOLDED = 0
    FOLDED = 1

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.state = FoldingIndicator.UNFOLDED


class FoldingPanel(Panel):
    DESCRIPTION = "Manage and draw folding indicators"
    IDENTIFIER = "foldingPanel"

    def __init__(self):
        Panel.__init__(self)
        self.__indicators = []
        self.scrollable = True
        self.setMouseTracking(True)
        self.__mouseOveredIndic = None
        self.__rightArrowIcon = (QtGui.QIcon(constants.ICON_ARROW_RIGHT[0]),
                                 QtGui.QIcon(constants.ICON_ARROW_RIGHT[1]))
        self.__downArrowIcon = (QtGui.QIcon(constants.ICON_ARROW_DOWN[0]),
                                QtGui.QIcon(constants.ICON_ARROW_DOWN[1]))
        # get the native fold scope color
        pal = self.palette()
        b = pal.base().color()
        h = pal.highlight().color()
        self.__systemColor = mergedColors(b, h, 50)
        self.__decorations = []

    def install(self, editor):
        Panel.install(self, editor)
        self.__native = self.editor.style.addProperty("nativeFoldingIndicator",
                                                      True)
        self.__color = self.editor.style.addProperty("foldIndicatorBackground",
                                                     self.__systemColor)
        self.__decoColor = driftColor(
            self.editor.style.value("panelBackground"))

    def onStyleChanged(self, section, key, value):
        Panel.onStyleChanged(self, section, key, value)
        if key == "nativeFoldingIndicator":
            self.__native = self.editor.style.value_from_str(value)
        elif key == "foldIndicatorBackground":
            self.__color = QtGui.QColor(value)
        elif key == "panelBackground":
            self.__decoColor = driftColor(QtGui.QColor(value))

    def resetScopeColor(self):
        self.editor.style.setValue(
            "foldIndicatorBackground", self.__systemColor)

    def addIndicator(self, indicator):
        """
        Adds the marker to the panel.

        :param indicator: Marker to add
        """
        self.__indicators.append(indicator)
        self.repaint()

    def removeIndicator(self, indicator):
        """
        Removes the marker from the panel

        :param indicator: Marker to remove
        """
        self.__indicators.remove(indicator)
        self.repaint()

    def clearIndicators(self):
        """ Clears the markers list """
        self.__indicators[:] = []
        self.repaint()

    def getIndicatorForLine(self, line):
        for indic in self.__indicators:
            if indic.start == line:
                return indic
        return None

    def getNearestIndicator(self, line):
        for indic in reversed(self.__indicators):
            if indic.start <= line <= indic.end:
                return indic
        return None

    def __foldRemaings(self, foldingIndicator):
        found = False
        for indic in self.__indicators:
            if indic == foldingIndicator:
                found = True
                continue
            if found:
                self.__fold(indic.start, indic.end,
                            indic.state == FoldingIndicator.FOLDED)

    def fold(self, foldingIndicator):
        self.__fold(foldingIndicator.start, foldingIndicator.end, fold=True)
        foldingIndicator.state = FoldingIndicator.FOLDED
        self.__foldRemaings(foldingIndicator)

    def unfold(self, foldingIndicator):
        self.__fold(foldingIndicator.start, foldingIndicator.end, fold=False)
        foldingIndicator.state = FoldingIndicator.UNFOLDED
        self.__foldRemaings(foldingIndicator)

    def __fold(self, start, end, fold=True):
        """ Folds/Unfolds a block of text delimitted by start/end line numbers

        :param start: Start folding line (this line is not fold, only the next
        ones)

        :param end: End folding line.

        :param fold: True to fold, False to unfold
        """
        print(fold)
        doc = self.editor.document()
        for i in range(start, end):
            block = self.editor.document().findBlockByNumber(i)
            block.setVisible(not fold)
            doc.markContentsDirty(block.position(), block.length())
        self.editor.refreshPanels()

    def __drawArrow(self, arrowRect, active, expanded, painter):
        if self.__native:
            opt = QtGui.QStyleOptionViewItemV2()
            opt.rect = arrowRect
            opt.state = (QtGui.QStyle.State_Active |
                         QtGui.QStyle.State_Item |
                         QtGui.QStyle.State_Children)
            if expanded:
                opt.state |= QtGui.QStyle.State_Open
            if active:
                opt.state |= (QtGui.QStyle.State_MouseOver |
                              QtGui.QStyle.State_Enabled |
                              QtGui.QStyle.State_Selected)
                opt.palette.setBrush(QtGui.QPalette.Window,
                                     self.palette().highlight())
            opt.rect.translate(-2, 0)
            self.style().drawPrimitive(QtGui.QStyle.PE_IndicatorBranch,
                                       opt, painter, self)
        else:
            index = 0
            if active:
                index = 1
            if expanded:
                self.__downArrowIcon[index].paint(painter, arrowRect)
            else:
                self.__rightArrowIcon[index].paint(painter, arrowRect)

    def __drawBackgroundRect(self, foldZoneRect, painter):
        c = self.__color
        grad = QtGui.QLinearGradient(foldZoneRect.topLeft(),
                                     foldZoneRect.topRight())
        grad.setColorAt(0, c.lighter(110))
        grad.setColorAt(1, c.lighter(130))
        outline = c
        painter.fillRect(foldZoneRect, grad)
        painter.setPen(QtGui.QPen(outline))
        painter.drawLine(foldZoneRect.topLeft() +
                         QtCore.QPoint(1, 0),
                         foldZoneRect.topRight() -
                         QtCore.QPoint(1, 0))
        painter.drawLine(foldZoneRect.bottomLeft() +
                         QtCore.QPoint(1, 0),
                         foldZoneRect.bottomRight() -
                         QtCore.QPoint(1, 0))
        painter.drawLine(foldZoneRect.topRight() +
                         QtCore.QPoint(0, 1),
                         foldZoneRect.bottomRight() -
                         QtCore.QPoint(0, 1))
        painter.drawLine(foldZoneRect.topLeft() +
                         QtCore.QPoint(0, 1),
                         foldZoneRect.bottomLeft() -
                         QtCore.QPoint(0, 1))

    def __clearDecorations(self):
        for d in self.__decorations:
            self.editor.removeDecoration(d)
        self.__decorations[:] = []
        return

    def __addDecorationsForIndic(self, indic):
        self.__mouseOveredIndic = indic
        tc = self.editor.textCursor()
        tc.movePosition(tc.Start, tc.MoveAnchor)
        tc.movePosition(tc.Down, tc.KeepAnchor, indic.start - 1)
        d = TextDecoration(tc)
        d.setFullWidth(True, clear=False)
        d.setBackground(self.__decoColor)
        self.editor.addDecoration(d)
        self.__decorations.append(d)
        tc.movePosition(tc.Start, tc.MoveAnchor)
        tc.movePosition(tc.Down, tc.MoveAnchor, indic.end)
        tc.movePosition(tc.End, tc.KeepAnchor)
        d = TextDecoration(tc)
        d.setFullWidth(True, clear=False)
        d.setBackground(self.__decoColor)
        self.editor.addDecoration(d)
        self.__decorations.append(d)

    def paintEvent(self, event):
        Panel.paintEvent(self, event)
        painter = QtGui.QPainter(self)
        for top, blockNumber in self.editor.visibleBlocks:
            indic = self.getIndicatorForLine(blockNumber)
            if indic:
                # compute rectangles
                arrowRect = QtCore.QRect(
                    0, top, self.sizeHint().width(), self.sizeHint().height())
                if indic.state == FoldingIndicator.UNFOLDED:
                    h = 0
                    for i in range(indic.start, indic.end + 1):
                        block = self.editor.document().findBlockByNumber(i)
                        if block.isVisible():
                            h += self.sizeHint().height()
                else:
                    h = self.sizeHint().height()
                foldZoneRect = QtCore.QRect(
                    0, top, self.sizeHint().width(), h)
                expanded = indic.state == FoldingIndicator.UNFOLDED
                active = indic == self.__mouseOveredIndic
                if active:
                    self.__drawBackgroundRect(foldZoneRect, painter)
                self.__drawArrow(arrowRect, active, expanded, painter)

    def sizeHint(self):
        """ Returns the widget size hint (based on the editor font size) """
        fm = QtGui.QFontMetricsF(self.editor.font())
        size_hint = QtCore.QSize(fm.height(), fm.height())
        if size_hint.width() > 16:
            size_hint.setWidth(16)
        return size_hint

    def mouseMoveEvent(self, event):
        line = self.editor.lineNumber(event.pos().y())
        if not line:
            self.__mouseOveredIndic = None
            return
        indic = self.getNearestIndicator(line)
        if indic != self.__mouseOveredIndic:
            self.__clearDecorations()
            if not indic:
                self.repaint()
                return
            self.__addDecorationsForIndic(indic)
            self.repaint()

    def mousePressEvent(self, event):
        if self.__mouseOveredIndic:
            if self.__mouseOveredIndic.state == FoldingIndicator.UNFOLDED:
                self.fold(self.__mouseOveredIndic)
            else:
                self.unfold(self.__mouseOveredIndic)

    def leaveEvent(self, e):
        self.__mouseOveredIndic = None
        self.__clearDecorations()
        self.repaint()


if __name__ == '__main__':
    from pcef.core import QGenericCodeEdit, constants, DelayJobRunner

    class Example(QGenericCodeEdit):

        def __init__(self):
            QGenericCodeEdit.__init__(self, parent=None)
            self.openFile(__file__)
            self.resize(QtCore.QSize(1000, 600))
            self.installPanel(FoldingPanel())
            self.foldingPanel.addIndicator(FoldingIndicator(21, 28))
            self.foldingPanel.addIndicator(FoldingIndicator(25, 28))
            fi = FoldingIndicator(35, 50)
            self.foldingPanel.addIndicator(fi)
            self.foldingPanel.fold(fi)
            self.foldingPanel.zoneOrder = -1

    import sys
    app = QtGui.QApplication(sys.argv)
    e = Example()
    e.show()
    sys.exit(app.exec_())

