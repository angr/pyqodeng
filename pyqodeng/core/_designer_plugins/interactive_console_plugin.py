# -*- coding: utf-8 -*-
"""
This module contains the InteractiveConsole designer plugin.
"""
from pyqodeng.core import widgets
from pyqodeng.core._designer_plugins import WidgetPlugin


class InteractiveConsolePlugin(WidgetPlugin):
    """
    Designer plugin for TabWidget.
    """
    def klass(self):
        return widgets.InteractiveConsole

    def objectName(self):
        return 'interactiveConsole'
