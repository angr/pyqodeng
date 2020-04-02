"""
Minimal example showing the use of the OccurrencesHighlighterMode.
"""
import logging
logging.basicConfig(level=logging.DEBUG)
import sys

from qtpy import QtWidgets
from pyqodeng.core.api import CodeEdit
from pyqodeng.core.backend import server
from pyqodeng.core.modes import OccurrencesHighlighterMode


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    editor = CodeEdit()
    editor.backend.start(server.__file__)
    editor.resize(800, 600)
    print(editor.modes.append(OccurrencesHighlighterMode()))
    editor.setPlainText(
        'mode\nmode\nmodes\npanel\nmode', '', '')
    editor.show()
    app.exec_()
    editor.close()
    del editor
    del app
