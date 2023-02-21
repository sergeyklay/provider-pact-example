#!/usr/bin/env python
#
# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""The main entry point for Specmatic Testing Example.

To run this entrypoint use any of the following command:

   $ flask --app runner:app run
   $ python runner.py
   $ ./runner.py

"""

import os

from products.app import create_app, load_env_vars

load_env_vars(os.path.dirname(os.path.abspath(__file__)))

# The application supports different startup modes:
#    - development
#    - testing
#    - production
#    - default (alias for development)
#
# To specify an application's startup mode, set the variable
# PRODUCTS_API_CONFIG to an appropriate value as follows:
#
#   $ export PRODUCTS_API_CONFIG=production
#   $ flask --app runner:app run
#
# Please note: When starting the application with flask script
# (which is by design the way to run an application in development mode),
# the --debug command line flag has nothing to do with the value of
# PRODUCTS_API_CONFIG variable because they are handled differently, by
# different subsystems. Thus, the following way of starting is perfectly
# functional (although it makes no sense):
#
#   $ export PRODUCTS_API_CONFIG=production
#   $ flask --app runner:app run --debug
#
config = os.getenv('PRODUCTS_API_CONFIG', 'default').lower()
app = create_app(config)

# The alternative way to start the application is through the Flask.run()
# method. This will immediately launch a local server exactly the same way
# the flask script does.
#
# The following code is for starting an application using only
# one of the following launch methods:
#
#   $ python runner.py
#   $ ./runner.py
#
# It will NOT be executed with the following launch methods:
#
#   $ flask --app runner:app run
#
if __name__ == '__main__':
    app.run()
