# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""A specialized application needed to run contract tests.

It contains additional endpoints to facilitate `provider_states`."""

from flask import jsonify
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


@app.route('/_pact/provider-states', methods=['POST'])
def provider_states():
    """Implement the "functionality" to change the state, to prepare for a test.

    When a Pact interaction is verified, it provides the "given" part of the
    description from the Consumer in the X_PACT_PROVIDER_STATES header.
    This can then be used to perform some operations on a database for example,
    so that the actual request can be performed and respond as expected.
    See: https://docs.pact.io/getting_started/provider_states

    This provider-states endpoint is deemed test only, and generally should not
    be available once deployed to an environment. It would represent both a
    potential data loss risk, and a security risk.

    As such, when running the Provider to test against, this is defined as the
    FLASK_APP to run, adding this additional route to the app while keeping the
    source separate.
    """
    return jsonify({'result': 'done'})


if __name__ == '__main__':
    app.run(debug=True, port=5001)