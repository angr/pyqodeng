from qtpy import QtCore
from qtpy.QtTest import QTest
from pyqodeng.core.api import TextHelper
from pyqodeng.core import modes


def get_mode(editor):
    return editor.modes.get(modes.AutoIndentMode)


def test_enabled(editor):
    mode = get_mode(editor)
    assert mode.enabled
    mode.enabled = False
    mode.enabled = True


def test_indent_eat_whitespaces(editor):
    editor.setPlainText('app = get_app(45, 4)', 'text/x-python', 'utf-8')
    TextHelper(editor).goto_line(0, 17)
    QTest.keyPress(editor, QtCore.Qt.Key_Return)
