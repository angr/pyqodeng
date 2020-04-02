"""
Show the use of the ErrorsTable widget.
"""
import sys
from qtpy import QtWidgets
from pyqodeng.core.modes import CheckerMessage, CheckerMessages
from pyqodeng.core.widgets import ErrorsTable

app = QtWidgets.QApplication(sys.argv)
table = ErrorsTable()
table.add_message(CheckerMessage(
    'A fake error message', CheckerMessages.ERROR, 10, path=__file__))
table.add_message(CheckerMessage(
    'A fake warning message', CheckerMessages.WARNING, 5, path=__file__))
table.show()
app.exec_()
