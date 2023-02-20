# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""The main entry point for Specmatic Testing Example.

To run this entrypoint use the following command:

   flask --app runner:app run

"""

import os

from products.app import create_app, load_env_vars

load_env_vars(os.path.dirname(os.path.abspath(__file__)))

config = os.getenv('APP_ENV', 'default').lower()
app = create_app(config)
