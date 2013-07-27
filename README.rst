PCEF - Python/Qt Code Editing Framework
=======================================

*version 1.0.0-beta.1*

.. image:: https://api.travis-ci.org/ColinDuquesnoy/pcef-core.png?branch=develop
    :target: https://travis-ci.org/ColinDuquesnoy/pcef-core
    :alt: Travis-CI build status

What is PCEF?
-------------

PCEF is a *flexible source code editing framework* for Python Qt
applications.

*pcef-core* is the foundation package, it contains everything you need
to create a generic (language independant) code editor widget and is the
mandatory requirement for any pcef extension.

The base widget (QCodeEdit) is a simple extension of QPlainTextEdit that
can be customised by adding extensions (modes and panels).

Features
--------

Here are the core features:

-  supports PySide and PyQt4
-  supports Python 2 and Python 3
-  simple widget based on QPlainTextEdit
-  easily customisable (modes and panels)
-  native look and feel close to Qt creator
-  builtin modes and panels (folding, line number, code completion,
   syntax highlighting)
-  Qt Designer plugin
-  `language specific extensions`_

.. _language specific extensions: https://github.com/ColinDuquesnoy/pcef-core/wiki/Extensions


License
-------

PCEF is licensed under the LGPL v3.

Requirements
------------

pcef-core depends on the following libraries:

-  PyQt4 or PySide
-  Python 2.7 or Python 3 (>= 3.2)
-  pygments
-  setuptools

Installation
------------

::

    $ pip install pcef-core

Usage
-----

Here is a `simple example using PyQt4`_:

.. code:: python

    # simple example using PyQt4
    import sys
    import PyQt4
    import pcef.core
    from PyQt4.QtGui import QApplication


    def main():
        app = QApplication(sys.argv)
        editor = pcef.core.QGenericCodeEdit()
        editor.openFile(__file__)
        editor.resize(800, 600)
        editor.show()
        return app.exec_()


    if __name__ == "__main__":
        sys.exit(main())

.. _simple example using PyQt4: https://gist.github.com/ColinDuquesnoy/6096185

Resources
---------

-  `Downloads`_
-  `Source repository`_
-  `Documentation version 0.2`_
-  `Wiki`_

.. _Downloads: https://github.com/ColinDuquesnoy/pcef-core/releases
.. _Source repository: https://github.com/ColinDuquesnoy/pcef-core/
.. _Documentation version 0.2: http://packages.python.org/PCEF
.. _Wiki: https://github.com/ColinDuquesnoy/pcef-core/wiki