#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for pyqodeng.core
"""
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from pyqodeng.core import __version__

#
# add ``build_ui command`` (optional, for development only)
# this command requires the following packages:
#   - pyqt-distutils
#   - pyqode-uic
#
import sys
import os
os.environ['DEB_BUILD_OPTIONS'] = 'nocheck'

try:
    from pyqt_distutils.build_ui import build_ui
    cmdclass = {'build_ui': build_ui}
except ImportError:
    cmdclass = {}


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ""

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        # force the use of boxed mode (each test will run in an isolated
        # process)
        if self.pytest_args:
            self.pytest_args = self.pytest_args.replace('"', '').split(' ')
        else:
            self.pytest_args = []
        if '--boxed' not in self.pytest_args:
            self.pytest_args.insert(0, '--boxed')
        print('running test command: py.test "%s"' % ' '.join(
            self.pytest_args))
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

cmdclass['test'] = PyTest


pygments_req = 'pygments'
if sys.version_info[0] == 3 and sys.version_info[1] == 2:
    # pygment 2 does not support Python 3.2
    pygments_req += "==1.6"


DESCRIPTION = 'PyQt/PySide Source Code Editor Widget'


def readme():
    if 'bdist_deb' in sys.argv or 'sdist_dsc' in sys.argv:
        return DESCRIPTION
    return str(open('README.rst').read())


setup(
    name='pyqodeng',
    namespace_packages=['pyqodeng'],
    version=__version__,
    packages=[p for p in find_packages() if 'test' not in p],
    keywords=["CodeEdit PyQt source code editor widget qt"],
    url='https://github.com/angr/pyqodeng',
    license='MIT',
    author='Colin Duquesnoy and others',
    author_email='colin.duquesnoy@gmail.com',
    description=DESCRIPTION,
    long_description=readme(),
    install_requires=[pygments_req, 'qtpy>=2.2.1', 'future', "PySide6-Essentials"],
    tests_require=['pytest-xdist', 'pytest-cov', 'pytest-pep8', 'pytest'],
    entry_points={
        'console_scripts': [
            'pyqode-console = pyqodeng.core.tools.console:main'
        ],
        'pyqode_plugins':
            ['code_edit = pyqodeng.core._designer_plugins'],
        'pygments.styles':
            ['qt = pyqodeng.core.styles.qt:QtStyle',
             'darcula = pyqodeng.core.styles.darcula:DarculaStyle']
    },
    zip_safe=False,
    cmdclass=cmdclass,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: Qt',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Widget Sets',
        'Topic :: Text Editors :: Integrated Development Environments (IDE)'])
