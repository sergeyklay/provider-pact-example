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

from flask_migrate import upgrade

from products.app import create_app, load_env_vars
from products.models import db
from products.seeder import seed_products

load_env_vars(os.path.dirname(os.path.abspath(__file__)))

config = os.getenv('FLASK_CONFIG', 'default').lower()
app = create_app(config)

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
    # Add seed data to the database if current mode is testing
    if config == 'testing':
        with app.app_context():
            db.session.remove()
            db.drop_all()
            upgrade()
            seed_products()
    app.run()
