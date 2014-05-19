import os
from pyqode.qt import QT_API
from pyqode.qt import PYQT5_API
from pyqode.qt import PYQT4_API
from pyqode.qt import PYSIDE_API

if os.environ[QT_API] == PYQT5_API:
    from PyQt5.QtCore import *
    from PyQt5.Qt import Qt
    from PyQt5.QtCore import pyqtSignal as Signal
    from PyQt5.QtCore import pyqtSlot as Slot
    from PyQt5.QtCore import pyqtProperty as Property
    from PyQt5.QtCore import QT_VERSION_STR as __version__
elif os.environ[QT_API] == PYQT4_API:
    from PyQt4.QtCore import *
    from PyQt4.Qt import Qt
    from PyQt4.QtCore import pyqtSignal as Signal
    from PyQt4.QtCore import pyqtSlot as Slot
    from PyQt4.QtCore import pyqtProperty as Property
    from PyQt4.QtCore import QT_VERSION_STR as __version__
elif os.environ[QT_API] == PYSIDE_API:
    from PySide.QtCore import *
    import PySide.QtCore
    __version__ = PySide.QtCore.__version__
    from PySide.QtCore import *
