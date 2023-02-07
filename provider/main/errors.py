# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""The error handler module for the application."""

from flask import json
from werkzeug.wrappers import Response
from werkzeug.exceptions import (
    HTTPException,
    BadRequest,
    NotFound,
    MethodNotAllowed
)

from provider.main import main



@main.errorhandler(HTTPException)
def handle_error(e: HTTPException) -> Response:
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({
        'code': e.code,
        'name': e.name,
        'description': e.description,
    })
    response.content_type = 'application/json'
    return response


@main.app_errorhandler(400)
def bad_request(e: HTTPException) -> Response:
    """Registers a function to handle 400 errors."""
    return handle_error(BadRequest(response=e.get_response()))


@main.app_errorhandler(404)
def page_not_found(e: HTTPException) -> Response:
    """Registers a function to handle 404 errors."""
    return handle_error(NotFound(response=e.get_response()))


@main.app_errorhandler(405)
def method_not_allowed(e: HTTPException) -> Response:
    """Registers a function to handle 405 errors."""
    return handle_error(MethodNotAllowed(response=e.get_response()))
