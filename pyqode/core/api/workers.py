#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#The MIT License (MIT)
#
#Copyright (c) <2013-2014> <Colin Duquesnoy and others, see AUTHORS.txt>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
#
"""
This module contains the worker functions/classes used on the server side.

A worker is a function or a callable which receive one single argument (the
decoded json object) and returns a tuple made up of a status (bool) and a
response object (json serialisable).

A worker is always tightly coupled with its caller, so are the data.

.. warning::
    This module should keep its dependencies as low as possible and fully
    supports python2 syntax. This is badly needed since the server might be run
    with a python2 interpreter. We don't want to force the user to install all
    the pyqode dependencies twice (if the user choose to run the server with
    python2, which might happen in pyqode.python to support python2 syntax).

"""
import sys
import traceback


def echo(data):
    """
    Example of worker that simply echoes back the received data.

    :returns: True, data
    """
    print('echo worker running')
    return True, data


class CodeCompletion(object):
    """
    This is the worker associated with the code completion mode.

    The worker does not actually do anything smart, the real work of collecting
    code completions is accomplished by the completion providers (see the
    :class:`pyqode.core.api.code_completion.Provider` interface)
    listed in :attr:`pyqode.core.api.workers.CompletionWorker.providers`.

    Those completion providers must be installed on the CodeCompletionWorker
    at the beginning of the main server script, e.g.::

        from pyqode.core.api import workers
        workers.CodeCompletion.providers.insert(0, MyProvider())
    """
    #: The list of code completion provider to run on each completion request.
    providers = []

    def __call__(self, data):
        """
        Do the work (this will be called in the child process by the
        SubprocessServer).
        """
        code = data['code']
        line = data['line']
        column = data['column']
        path = data['path']
        encoding = data['encoding']
        prefix = data['prefix']
        completions = []
        for prov in CodeCompletion.providers:
            try:
                completions.append(prov.complete(
                    code, line, column, prefix, path, encoding))
                if len(completions) > 20:
                    break
            except :
                sys.stderr.write('Failed to get completions from provider %r'
                                 % prov)
                e1, e2, e3 = sys.exc_info()
                traceback.print_exception(e1, e2, e3, file=sys.stderr)
        return True, completions