#!/usr/bin/env bash

# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

set -o pipefail

if [ -z "${PYENV_VIRTUAL_ENV}" ]; then
  python="${PYTHON:-$(command -v python3 2>/dev/null)}"
else
  python="${PYTHON:-$(pyenv which python 2>/dev/null)}"
fi

PORT=5001

# Run the Flask server, using the 'tests/app.py' as the app to be able to
# inject the '-pact/provider-states' endpoint
FLASK_APP=tests/app.py $python -m flask run -p $PORT &
FLASK_PID=$!

# Make sure the Flask server is stopped when finished to avoid blocking the port
function teardown {
  echo "Tearing down Flask server: ${FLASK_PID}"
  kill -9 $FLASK_PID 2>/dev/null || true
}
trap teardown EXIT

# Wait a little in case Flask isn't quite ready
while ! nc -z localhost $PORT; do
  sleep 0.1
done

# Turn off the annoying warning in the output
PACT_DO_NOT_TRACK=true
export PACT_DO_NOT_TRACK

# Now run the tests
$python -m pytest tests --verbose -o log_cli=true -m contracts
