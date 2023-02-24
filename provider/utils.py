# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""A module with utility functions."""

from flask import jsonify, Response

_BOOL_MAP = {
    'y': True,
    'yes': True,
    't': True,
    'true': True,
    'on': True,
    '1': True,
    'n': False,
    'no': False,
    'f': False,
    'false': False,
    'off': False,
    '0': False
}


def strtobool(value):
    try:
        return _BOOL_MAP[str(value).lower()]
    except KeyError as exc:
        raise ValueError(f'''"{value}" is not a valid bool value''') from exc


def json_response(status: int, title: str, description: str) -> Response:
    """Make JSON response."""
    response = jsonify({'status': status, 'title': title,
                        'description': description})
    response.status_code = status
    return response
