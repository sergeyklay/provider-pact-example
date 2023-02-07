# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""The main blueprint module for the application.

Provides the routes and errors handlers definition for the
application.

"""

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
