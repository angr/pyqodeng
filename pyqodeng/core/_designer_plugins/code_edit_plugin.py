# -*- coding: utf-8 -*-
"""
This module contains the CodeEdit designer plugin.
"""
from pyqodeng.core._designer_plugins import WidgetPlugin
from pyqodeng.core.api import CodeEdit


class CodeEditPlugin(WidgetPlugin):
    """
    Designer plugin for CodeEdit.
    """
    def klass(self):
        return CodeEdit

    def objectName(self):
        return 'codeEdit'
