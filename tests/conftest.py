# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

import pytest
from flask_migrate import upgrade

from provider.app import create_app, db


@pytest.fixture()
def app():
    app_instance = create_app('testing')
    app_instance.config.update({
        'TESTING': True,
    })
    with app_instance.app_context():
        db.session.remove()
        db.drop_all()
        upgrade()

        yield app_instance

        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
