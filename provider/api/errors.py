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


@api.errorhandler(Exception)
def handle_500(error: Exception):
    """Registers a function to handle base Exception."""
    exc = HTTPException()
    exc.description = error.args[0]
    exc.code = 500

    return ErrorHandlerMixin().handle_http_exception(exc)
