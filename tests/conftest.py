# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

import os
import subprocess

import pytest
from flask_migrate import upgrade

from provider import __version__ as tag
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


def git_revision_short_hash() -> str:
    root = os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))
    )

    return subprocess.check_output(
        ['git', '-C', root, 'rev-parse', '--short', 'HEAD']
    ).decode('ascii').strip()


@pytest.fixture()
def participant_version() -> str:
    """Get participant version number.

    To get the most out of the Pact Broker, it should either be the git sha
    (or equivalent for your repository), be a git tag name, or it should
    include the git sha or tag name as metadata if you are using semantic
    versioning eg. 1.2.456+405b31ec6.

    See: https://docs.pact.io/pact_broker/pacticipant_version_numbers for more
    details."""
    commit = git_revision_short_hash()
    return f'{tag}-{commit}'
