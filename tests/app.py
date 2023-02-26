# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""A specialized application needed to run contract tests.

It contains additional endpoints to facilitate `provider_states`."""

from flask_migrate import upgrade

from provider.app import create_app, db
from provider.seeder import seed_products

app = create_app('testing')
app.config.update({
    'DEBUG': True,
    'TESTING': True,
})

with app.app_context():
    db.session.remove()
    db.drop_all()
    upgrade()
    seed_products()
