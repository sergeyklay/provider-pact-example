import functools
from flask import jsonify
from flask_sqlalchemy.query import Query


def json(f):
    """Generate a JSON response from a database model or a Python
        dictionary."""
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        # invoke the wrapped function
        rv = f(*args, **kwargs)

        # the wrapped function can return the dictionary alone,
        # or can also include a status code and/or headers.
        # here we separate all these items
        status = None
        headers = None
        if isinstance(rv, tuple):
            rv, status, headers = rv + (None,) * (3 - len(rv))
        if isinstance(status, (dict, list)):
            headers, status = status, None

        if not isinstance(rv, dict):
            # if the response was a Query instance, then convert it to a
            # dictionary
            if isinstance(rv, Query):
                rv = [item.export_data() for item in rv]
            # if the response was a database model, then convert it to a
            # dictionary
            else:
                rv = rv.export_data()

        # generate the JSON response
        rv = jsonify(rv)
        if status is not None:
            rv.status_code = status
        if headers is not None:
            rv.headers.extend(headers)
        return rv

    return wrapped
