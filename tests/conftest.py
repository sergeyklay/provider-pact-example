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

from provider import __version__ as version
from provider.app import create_app


@pytest.fixture()
def app():
    app_instance = create_app('testing')
    app_instance.config.update({
        'TESTING': True,
    })
    with app_instance.app_context():
        upgrade()
        yield app_instance


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def git_revision_short_hash() -> str:
    """Get the short Git commit."""
    root = os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))
    )

    return subprocess.check_output(
        ['git', '-C', root, 'rev-parse', '--short', 'HEAD']
    ).decode('ascii').strip()


@pytest.fixture()
def app_version() -> str:
    """Get participant version number.

    To get the most out of the Pact Broker, it should either be the git sha
    (or equivalent for your repository), be a git tag name, or it should
    include the git sha or tag name as metadata if you are using semantic
    versioning eg. 1.2.456+405b31ec6.

    See https://docs.pact.io/pact_broker/pacticipant_version_numbers for more
    details."""
    git_commit = git_revision_short_hash()
    return f'{version}+{git_commit}'
