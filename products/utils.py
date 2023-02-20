# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""A module with utility functions."""

from flask import jsonify, Response


def json_response(status: int, title: str, description: str) -> Response:
    """Make JSON response."""
    response = jsonify({'status': status, 'title': title,
                        'description': description})
    response.status_code = status
    return response
