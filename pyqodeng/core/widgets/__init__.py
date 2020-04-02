# -*- coding: utf-8 -*-
"""
This package contains a set of widgets that might be useful when writing
pyqode applications:

    - TextCodeEdit: code edit specialised for plain text
    - GenericCodeEdit: generic code edit, using PygmentsSH.
      Not really fast, not really smart.
    - InteractiveConsole: QTextEdit made for running background process
      interactively. Can be used in an IDE for running programs or to display
      the compiler output,...
    - CodeEditTabWidget: tab widget made to handle CodeEdit instances (or
      any other object that have the same interface).
    - ErrorsTable: a QTableWidget specialised to show CheckerMessage.
    - OutlineTreeWidget: a widget that show the outline of an editor.


"""
from pyqodeng.core.widgets.code_edits import TextCodeEdit, GenericCodeEdit
from pyqodeng.core.widgets.encodings import (EncodingsComboBox, EncodingsMenu,
                                             EncodingsContextMenu)
from pyqodeng.core.widgets.errors_table import ErrorsTable
from pyqodeng.core.widgets.file_icons_provider import FileIconProvider
from pyqodeng.core.widgets.interactive import InteractiveConsole  # Deprecated
from pyqodeng.core.widgets.menu_recents import MenuRecentFiles
from pyqodeng.core.widgets.menu_recents import RecentFilesManager
from pyqodeng.core.widgets.preview import HtmlPreviewWidget
from pyqodeng.core.widgets.tabs import TabWidget
from pyqodeng.core.widgets.tab_bar import TabBar
from pyqodeng.core.widgets.prompt_line_edit import PromptLineEdit
from pyqodeng.core.widgets.outline import OutlineTreeWidget
from pyqodeng.core.widgets.splittable_tab_widget import (
    SplittableTabWidget, SplittableCodeEditTabWidget)
from pyqodeng.core.widgets.filesystem_treeview import FileSystemTreeView
from pyqodeng.core.widgets.filesystem_treeview import FileSystemContextMenu
from pyqodeng.core.widgets.filesystem_treeview import FileSystemHelper
from pyqodeng.core.widgets.output_window import OutputWindow
from pyqodeng.core.widgets.terminal import Terminal


__all__ = [
    'ErrorsTable',
    'FileSystemContextMenu',
    'FileSystemTreeView',
    'InteractiveConsole',
    'FileIconProvider',
    'FileSystemHelper',
    'MenuRecentFiles',
    'RecentFilesManager',
    'TabWidget',
    'EncodingsComboBox',
    'EncodingsMenu',
    'EncodingsContextMenu',
    'TextCodeEdit',
    'GenericCodeEdit',
    'PromptLineEdit',
    'OutlineTreeWidget',
    'SplittableTabWidget',
    'SplittableCodeEditTabWidget',
    'TabBar',
    'HtmlPreviewWidget',
    'OutputWindow',
    'Terminal'
]
