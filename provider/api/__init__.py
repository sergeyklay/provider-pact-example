# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""The api blueprint module for the application."""

from flask import Blueprint
from flask import request, Response

from provider.decorators import etag

api = Blueprint('api', __name__)


@api.after_request
@etag
def after_request(response):
    """Generate an ETag header for all routes in this blueprint."""
    return response


@api.before_request
# pylint: disable-next=inconsistent-return-statements
def specmatic_deletes_product():
    """Emulate deletion for testing purposes.
     Actually this method is needed only for contract testing."""
    if request.method == 'DELETE' and request.view_args['product_id'] == 7777:
        # Specmatic uses User-Agent 'Ktor client'
        if request.headers.get('User-Agent') == 'Ktor client':
            return Response(status=204)


from . import errors, products  # noqa: I100, I202, F401, E402
