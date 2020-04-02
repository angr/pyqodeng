# -*- coding: utf-8 -*-
"""
This module contains the TabWidget designer plugin.
"""
from pyqodeng.core import widgets
from pyqodeng.core._designer_plugins import WidgetPlugin


class TabWidgetPlugin(WidgetPlugin):
    """
    Designer plugin for TabWidget.
    """
    def klass(self):
        return widgets.TabWidget

    def objectName(self):
        return 'tabWidget'
