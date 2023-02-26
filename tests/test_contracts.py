# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

from os import environ

import pytest
from pact import Verifier

from provider import __version__ as version

# For the purposes of this example, the broker is started up using docker
# compose (see '.github/workflows/test-contracts.yaml'). For normal usage this
# would be self-hosted or using PactFlow.
PACT_BROKER_URL = environ.get('PACT_BROKER_URL', 'http://localhost')
PACT_BROKER_USERNAME = environ.get('PACT_BROKER_USERNAME', 'pactbroker')
PACT_BROKER_PASSWORD = environ.get('PACT_BROKER_PASSWORD', 'pactbroker')

# For the purposes of this example, the Flask provider will be started up as a
# part of 'tests/run-pytest.sh' when running the tests. Alternatives could be,
# for example running a Docker container with a DB of test data configured.
# This is the "real" provider to verify against.
PROVIDER_HOST = 'localhost'
PROVIDER_PORT = 5001
PROVIDER_URL = f'http://{PROVIDER_HOST}:{PROVIDER_PORT}'


@pytest.fixture
def broker_opts():
    return {
        'broker_username': PACT_BROKER_USERNAME,
        'broker_password': PACT_BROKER_PASSWORD,
        'broker_url': PACT_BROKER_URL,
        'publish_version': version,
        'publish_verification_results': True,
    }


@pytest.mark.contracts
def test_product_service_provider_against_broker(broker_opts):
    verifier = Verifier(
        provider='ProductService',
        provider_base_url=PROVIDER_URL,
    )

    success, logs = verifier.verify_with_broker(
        **broker_opts,
        verbose=True,
        # TODO: enable this
        # provider_states_setup_url=f"{PROVIDER_URL}/_pact/provider_states",
        enable_pending=False,
    )
    assert success == 0
