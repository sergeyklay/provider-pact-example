# This file is part of the Contract Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Provides all decorators used for the application."""

from .caching import etag  # noqa: F401
from .json import json  # noqa: F401
from .paginate import paginate  # noqa: F401
