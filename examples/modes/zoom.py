"""
Minimal example showing the use of the ZoomMode.
"""
import logging
logging.basicConfig(level=logging.DEBUG)
import sys

from qtpy import QtWidgets
from pyqodeng.core.api import CodeEdit
from pyqodeng.core.backend import server
from pyqodeng.core.modes import ZoomMode


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    editor = CodeEdit()
    editor.backend.start(server.__file__)
    editor.resize(800, 600)
    print(editor.modes.append(ZoomMode()))
    editor.appendPlainText(
        'Use Ctrl+Mouse wheel to zoom in/out\n'
        'Ctrl++ and Ctrl+- can also be used\n'
        'Ctrl+0 resets the editor zoom level to 0')
    editor.show()
    app.exec_()
    editor.close()
    del editor
    del app
