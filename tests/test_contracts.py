# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

import pytest
from pact import Verifier

from provider import __version__ as version

PROVIDER_HOST = 'localhost'
PROVIDER_PORT = 5001
PROVIDER_URL = f'http://{PROVIDER_HOST}:{PROVIDER_PORT}'


@pytest.fixture
def broker_opts():
    # TODO: remove hardcode here
    return {
        'broker_username': 'pactbroker',
        'broker_password': 'pactbroker',
        'broker_url': 'http://127.0.0.1',
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
