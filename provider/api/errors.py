# This file is part of the Contract Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""The error handler module for the application."""

from flask import current_app
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from werkzeug.exceptions import HTTPException, InternalServerError
from werkzeug.wrappers import Response

from provider.exceptions import ValidationError
from provider.utils import json_response
from . import api


@api.errorhandler(ValidationError)
def validation_error(error: HTTPException):
    """Registers a function to handle validation errors."""
    return json_response(400, 'Validation Error', error.args[0])


@api.app_errorhandler(IntegrityError)
def sqlalchemy_integrity_error(error: IntegrityError):
    return json_response(400, 'Database integrity error', str(error.orig))


@api.app_errorhandler(SQLAlchemyError)
def sqlalchemy_error(error):
    if current_app.config['DEBUG'] is True:
        return json_response(500, 'Database error', str(error))
    return json_response(
        InternalServerError.code,
        InternalServerError().name,
        InternalServerError.description,
    )


@api.app_errorhandler(400)
def bad_request(error: HTTPException) -> Response:
    """Registers a function to handle 400 errors."""
    return json_response(400, 'Bad Request', error.description)


@api.app_errorhandler(404)
def page_not_found(_error: HTTPException) -> Response:
    """Registers a function to handle 404 errors."""
    return json_response(404, 'Not Found', 'Invalid resource URI.')


@api.app_errorhandler(405)
def method_not_supported(error: HTTPException) -> Response:
    """Registers a function to handle 405 errors."""
    return json_response(
        error.code,
        error.name,
        error.description,
    )


@api.app_errorhandler(500)
def internal_server_error(error: HTTPException) -> Response:
    """Registers a function to handle 500 errors."""
    return json_response(
        error.code,
        error.name,
        error.description,
    )


@api.app_errorhandler(503)
def service_unavailable(error: HTTPException) -> Response:
    """Registers a function to handle 503 errors."""
    return json_response(
        error.code,
        error.name,
        error.description,
    )
