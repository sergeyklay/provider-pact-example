# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Provides caching decorators."""

import functools
import hashlib

from flask import make_response, request

from provider.utils import json_response


def etag(func):
    """Add entity tag (etag) handling to the decorated route."""
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        # invoke the wrapped function and generate a response object from
        # its result
        rv = func(*args, **kwargs)
        rv = make_response(rv)

        # etags only make sense for request that are cacheable, so only
        # GET and HEAD requests are allowed
        if request.method not in ['GET', 'HEAD']:
            return rv

        # if the response is not a code 200 OK then we let it through
        # unchanged
        if rv.status_code != 200:
            return rv

        # compute the etag for this request as the MD5 hash of the response
        # text and set it in the response header
        etag_val = '"' + hashlib.md5(rv.get_data()).hexdigest() + '"'
        rv.headers['ETag'] = etag_val

        # handle If-Match and If-None-Match request headers if present
        if_match = request.headers.get('If-Match')
        if_none_match = request.headers.get('If-None-Match')

        if if_match:
            # only return the response if the etag for this request matches
            # any of the etags given in the If-Match header. If there is no
            # match, then return a 412 Precondition Failed status code
            etag_list = [tag.strip() for tag in if_match.split(',')]
            if etag not in etag_list and '*' not in etag_list:
                return json_response(412, 'Precondition Failed',
                                     'Precondition Failed.')
        elif if_none_match:
            # only return the response if the etag for this request does not
            # match any of the etags given in the If-None-Match header. If
            # one matches, then return a 304 Not Modified status code
            etag_list = [tag.strip() for tag in if_none_match.split(',')]
            if etag in etag_list or '*' in etag_list:
                return json_response(304, 'Not Modified',
                                     'Resource not modified.')
        return rv
    return wrapped
