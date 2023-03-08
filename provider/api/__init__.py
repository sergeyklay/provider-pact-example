# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""The api blueprint module for the application."""

from flask_smorest import Blueprint

api = Blueprint(
    'api',
    __name__,
    url_prefix='/v2',
    description='Provider-side demo using consumer-driven contract testing'
)

from . import products  # noqa: I100, I202, F401, E402
