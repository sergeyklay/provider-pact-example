# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Provides json decorator to return API response."""

import functools

from flask import jsonify


def json(func):
    """Generate a JSON response from a database model or a Python
        dictionary."""
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        # invoke the wrapped function
        rv = func(*args, **kwargs)

        # the wrapped function can return the dictionary alone,
        # or can also include a status code and/or headers.
        # here we separate all these items
        status = None
        headers = None
        if isinstance(rv, tuple):
            rv, status, headers = rv + (None,) * (3 - len(rv))
        if isinstance(status, (dict, list)):
            headers, status = status, None

        # if the response was a database model, then convert it to a
        # dictionary
        if not isinstance(rv, dict):
            rv = rv.export_data()

        # generate the JSON response
        rv = jsonify(rv)
        if status is not None:
            rv.status_code = status
        if headers is not None:
            rv.headers.extend(headers)
        return rv

    return wrapped
