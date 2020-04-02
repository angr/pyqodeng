"""
This example will show you that the caret line color is automatically set
by the syntax highlighter mode.

See how the color is different from the color obtained in
``caret_line_highligter.py``
"""
import logging
logging.basicConfig(level=logging.DEBUG)
import sys

from qtpy import QtWidgets
from pyqodeng.core.api import CodeEdit
from pyqodeng.core.backend import server
from pyqodeng.core.modes import CaretLineHighlighterMode
from pyqodeng.core.modes import PygmentsSyntaxHighlighter


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    editor = CodeEdit()
    editor.backend.start(server.__file__)
    editor.resize(800, 600)
    print(editor.modes.append(CaretLineHighlighterMode()))
    print(editor.modes.append(PygmentsSyntaxHighlighter(editor.document())))
    editor.show()
    editor.appendPlainText('\n' * 10)
    app.exec_()
    editor.close()
    del editor
    del app
