"""
Minimal example showing the use of the FoldingPanel.

"""
import logging
logging.basicConfig(level=logging.DEBUG)
import sys

from qtpy import QtWidgets
from pyqodeng.core.api import CodeEdit, IndentFoldDetector
from pyqodeng.core.backend import server
from pyqodeng.core.modes import PygmentsSH
from pyqodeng.core.panels import FoldingPanel


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    editor = CodeEdit()
    editor.backend.start(server.__file__)
    editor.file.open(__file__)
    editor.resize(800, 600)
    # code folding panel will fetch data from the text block user state. That
    # state is set by a FoldDetector at highlight time. That means that to use
    # the folding panel, we must first set a syntax highlighter on CodeEdit and
    # set a FoldDetector on the installed syntax highlighter.
    sh = editor.modes.append(PygmentsSH(editor.document()))
    sh.fold_detector = IndentFoldDetector()
    # now we can add our folding panel
    editor.panels.append(FoldingPanel())
    editor.show()
    app.exec_()
    editor.close()
    del editor
    del app
