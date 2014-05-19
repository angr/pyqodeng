# -*- coding: utf-8 -*-
"""
This scripts configures the test suite. We do two things:

    - setup the logging module
    - create ONE SINGLE INSTANCE of QApplication:
      this implies that you must use **QApplication.instance** in your
      test scripts.
"""
import logging
import os
import sys
import pytest
import time

try:
    import faulthandler
    faulthandler.enable()
except ImportError:
    pass


# -------------------
# Setup runtest
# -------------------
def pytest_runtest_setup(item):
    """
    Skips tesks marker with a ``skip_on_travis`` marker.
    """
    if isinstance(item, item.Function):
        travis_platform = True if 'TRAVIS' in os.environ else False
        if travis_platform and item.get_marker('skip_on_travis'):
            pytest.skip("test skipped when ran on Travis-CI: %r" % item)


# -------------------
# Setup logging
# -------------------
logging.basicConfig(level=logging.DEBUG,
                    filename='pytest.log',
                    filemode='w')

# -------------------
# Setup QApplication
# -------------------
# 2. create qt application
from pyqode.qt.QtWidgets import QApplication
_app = QApplication(sys.argv)
_widget = None


# -------------------
# Session fixtures
# -------------------
@pytest.fixture(scope="session")
def app(request):
    global _app
    return app


@pytest.fixture(scope="session")
def editor(request):
    global _app, _widget
    from test import helpers
    from pyqode.core import frontend, settings

    logging.info('setup session editor')

    settings.file_watcher_auto_reload = True
    settings.save_on_focus_out = False

    _widget = frontend.CodeEdit()
    frontend.start_server(_widget, helpers.server_path())
    helpers.wait_for_connected(_widget)
    helpers.setup_editor(_widget)
    _widget.show()
    _widget.resize(800, 600)
    _app.setActiveWindow(_widget)

    def fin():
        global _widget
        logging.info('teardown session editor')
        frontend.stop_server(_widget)
        del _widget

    request.addfinalizer(fin)

    return _widget
