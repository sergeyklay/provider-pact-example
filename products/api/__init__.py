# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""The api blueprint module for the application."""

from flask import Blueprint

from products.decorators import etag

api = Blueprint('api', __name__)


@api.after_request
@etag
def after_request(response):
    """Generate an ETag header for all routes in this blueprint."""
    return response


from . import products, errors
