# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Module for Contracts (Pacts) verification."""

from os import environ

import pytest
from pact import Verifier


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
def broker_opts(app_version: str) -> dict:
    return {
        'broker_username': PACT_BROKER_USERNAME,
        'broker_password': PACT_BROKER_PASSWORD,
        'broker_url': PACT_BROKER_URL,
        'publish_version': app_version,
        'publish_verification_results': True,
    }


@pytest.mark.contracts
def test_product_service_provider_against_broker(broker_opts: dict):
    verifier = Verifier(
        provider='ProductService',
        provider_base_url=PROVIDER_URL,
    )

    # Request all Pact(s) from the Pact Broker to verify this Provider against.
    # In the Pact Broker logs, this corresponds to the following entry:
    #
    #    PactBroker::Api::Resources::ProviderPactsForVerification -- \
    #    Fetching pacts for verification by ProductService -- \
    #    {:provider_name=>"ProductService", \
    #    :params=>{"includePendingStatus"=>false}}
    #
    success, logs = verifier.verify_with_broker(
        **broker_opts,
        verbose=False,
        provider_states_setup_url=f"{PROVIDER_URL}/-pact/provider-states",
        enable_pending=False,
    )

    # If publish_verification_results is set to True, the results will be
    # published to the Pact Broker. In the Pact Broker logs, this corresponds
    # to the following entry:
    #
    #    PactBroker::Verifications::Service -- Creating verification 200 for \
    #    pact_version_sha=c8568cbb30d2e3933b2df4d6e1248b3d37f3be34 -- \
    #    {"success"=>true, "providerApplicationVersion"=>"1.8.0+dc939d3", \
    #    "wip"=>false, "pending"=>"true"}
    #

    # Note:
    #
    #  If "successful", then the return code here will be 0.
    #  This can still be 0 and so PASS if a Pact verification FAILS, as long as
    #  it has not resulted in a REGRESSION of an already verified interaction.
    #  See https://docs.pact.io/pact_broker/advanced_topics/pending_pacts/ for
    #  more details.
    assert success == 0
