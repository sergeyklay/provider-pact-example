# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""The error handler module for the application."""

from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import Response

from products.utils import json_response
from . import api


@api.app_errorhandler(400)
def bad_request(_error: HTTPException) -> Response:
    """Registers a function to handle 400 errors."""
    return json_response(404, 'Bad Request', 'Bad Request.')


@api.app_errorhandler(404)
def page_not_found(_error: HTTPException) -> Response:
    """Registers a function to handle 404 errors."""
    return json_response(404, 'Not Found', 'Invalid resource URI.')


@api.app_errorhandler(405)
def method_not_supported(_error: HTTPException) -> Response:
    """Registers a function to handle 405 errors."""
    return json_response(405, 'Method Not Allowed',
                         'The method is not supported.')


@api.app_errorhandler(500)
def internal_server_error(error: HTTPException) -> Response:
    """Registers a function to handle 500 errors."""
    return json_response(500, 'Internal Server Error',
                         error.description or '')


@api.app_errorhandler(503)
def service_unavailable(_error: HTTPException) -> Response:
    """Registers a function to handle 503 errors."""
    return json_response(503, 'Service Unavailable',
                         'The server is not ready to handle the request.')
