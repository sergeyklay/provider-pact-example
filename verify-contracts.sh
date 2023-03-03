#!/usr/bin/env bash

# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

set -o pipefail

PROJECT_ROOT=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

if [ -z "${PYENV_VIRTUAL_ENV}" ]; then
  PYTHON="${PYTHON:-$(command -v python3 2>/dev/null)}"
else
  PYTHON="${PYTHON:-$(pyenv which python 2>/dev/null)}"
fi

# To get the most out of the Pact Broker, it should either be the git sha
# (or equivalent for your repository), be a git tag name, or it should
# include the git sha or tag name as metadata if you are using semantic
# versioning eg. 1.2.456+405b31ec6.
#
# See https://docs.pact.io/pact_broker/pacticipant_version_numbers for more
# details.
APP_VERSION="$($PYTHON setup.py --version)"
APP_VERSION+="+$(git -C "$PROJECT_ROOT" rev-parse --short HEAD)"

# For the purposes of this example, the broker is started up using docker
# compose (see '.github/workflows/test-contracts.yaml'). For normal usage this
# would be self-hosted or using PactFlow.
PACT_BROKER_USERNAME="${PACT_BROKER_USERNAME:-pactbroker}"
PACT_BROKER_PASSWORD="${PACT_BROKER_PASSWORD:-pactbroker}"
PACT_BROKER_BASE_URL="${PACT_BROKER_BASE_URL:-http://localhost}"
export PACT_BROKER_USERNAME PACT_BROKER_PASSWORD PACT_BROKER_BASE_URL

# For the purposes of this example, the Flask server will be started up as a
# part of this script when running the tests. Alternatives could be,
# for example running a Docker container with a DB of test data configured.
# This is the "real" provider to verify against.
PROVIDER_HOST="${PROVIDER_HOST:-127.0.0.1}"
PROVIDER_PORT="${PROVIDER_PORT:-5001}"
PROVIDER_TRANSPORT="${PROVIDER_TRANSPORT:-http}"

# This will disable console messages for the 'tests/app.py'.
TEST_MODE="verify"
export TEST_MODE

# Run the Flask server, using the 'tests/app.py' as the app to be able to
# inject the '-pact/provider-states' endpoint
FLASK_APP="$PROJECT_ROOT/tests/app.py"
export FLASK_APP

$PYTHON -m flask run \
  --port "$PROVIDER_PORT" \
  --host "$PROVIDER_HOST" &
FLASK_PID=$!

# Make sure the Flask server is stopped when finished to avoid blocking the port
function teardown {
  echo "Tearing down Flask server: ${FLASK_PID}"
  kill -9 $FLASK_PID 2>/dev/null || true
}
trap teardown EXIT

# Wait a little in case Flask isn't quite ready
sleep 1

# Turn off the annoying warning in the output
PACT_DO_NOT_TRACK=true
export PACT_DO_NOT_TRACK

pact_verifier_cli \
  --provider-name ProductService \
  --provider-version "$APP_VERSION" \
  --provider-branch="$(git -C "$PROJECT_ROOT" rev-parse --abbrev-ref HEAD)" \
  --hostname "$PROVIDER_HOST" \
  --transport "$PROVIDER_TRANSPORT" \
  --port "$PROVIDER_PORT" \
  --disable-ssl-verification \
  --state-change-url "${PROVIDER_TRANSPORT}://${PROVIDER_HOST}:${PROVIDER_PORT}/-pact/provider-states" \
  --header User-Agent=PactBroker \
  --publish \
  --enable-pending \
  --ignore-no-pacts-error \
  --loglevel info
