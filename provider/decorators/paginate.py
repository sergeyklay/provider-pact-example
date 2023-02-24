# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Provides decorator to paginate API response."""

import functools

from flask import abort, request, url_for


def paginate(collection, max_per_page=10):
    """Generate a paginated response for a resource collection.

    Routes that use this decorator must return a SQLAlchemy query as a
    response.

    The output of this decorator is a Python dictionary with the paginated
    results. The application must ensure that this result is converted to a
    response object, either by chaining another decorator or by using a
    custom response object that accepts dictionaries."""
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            # invoke the wrapped function
            query = func(*args, **kwargs)

            # obtain pagination arguments from the URL's query string
            page = request.args.get('page', 1, type=int)
            if page < 1:
                message = ("The 'page' parameter cannot be less than 1, "
                           f'received: {page}.')
                abort(400, message)

            per_page = min(request.args.get('per_page', max_per_page,
                                            type=int), max_per_page)
            expanded = None
            if request.args.get('expanded', 0, type=int) != 0:
                expanded = 1

            # run the query with Flask-SQLAlchemy's pagination
            p = query.paginate(page=page, per_page=per_page)

            # build the pagination metadata to include in the response
            pages = {
                'page': page,
                'per_page': per_page,
                'total': p.total,
                'pages': p.pages or 1,  # can't be 0
            }

            links = {
                'self': request.url,
                'prev': None,
                'next': None,
            }

            kwargs.update(request.args)
            kwargs.pop('page', None)
            kwargs.pop('per_page', None)
            kwargs.pop('expanded', None)

            if p.has_prev:
                links['prev'] = url_for(
                    request.endpoint,
                    page=p.prev_num,
                    per_page=per_page,
                    expanded=expanded,
                    _external=True,
                    **kwargs,
                )

            if p.has_next:
                links['next'] = url_for(
                    request.endpoint,
                    page=p.next_num,
                    per_page=per_page,
                    expanded=expanded,
                    _external=True,
                    **kwargs,
                )

            links['first'] = url_for(
                request.endpoint,
                page=1,
                per_page=per_page,
                expanded=expanded,
                _external=True,
                **kwargs,
            )
            links['last'] = url_for(
                request.endpoint,
                page=p.pages or 1,  # can't be 0
                per_page=per_page,
                expanded=expanded,
                _external=True,
                **kwargs,
            )

            # generate the paginated collection as a dictionary
            if expanded:
                results = [item.export_data() for item in p.items]
            else:
                results = [item.get_url() for item in p.items]

            # return a dictionary as a response
            return {
                collection: results,
                'pagination': pages,
                'links': links,
            }
        return wrapped
    return decorator
