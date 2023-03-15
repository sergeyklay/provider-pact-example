# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""The error handler module for the application."""

from flask_smorest.error_handler import ErrorHandlerMixin
from werkzeug.exceptions import HTTPException

from . import api


def handle_application_error(error: Exception):
    """Handle Exception derivatives."""
    exc = HTTPException()
    exc.description = error.args[0]
    exc.code = 500

    return ErrorHandlerMixin().handle_http_exception(exc)


@api.errorhandler(AttributeError)
def handle_attribute_error(error: AttributeError):
    """Registers a function to handle AttributeError."""
    return handle_application_error(error)


@api.errorhandler(TypeError)
def handle_type_error(error: TypeError):
    """Registers a function to handle TypeError."""
    return handle_application_error(error)
