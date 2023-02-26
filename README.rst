.. raw:: html

    <h1 align="center">Provider API Example</h1>
    <p align="center">
        <a href="https://github.com/sergeyklay/provider-pact-example/actions/workflows/test-contracts.yaml">
            <img src="https://github.com/sergeyklay/provider-pact-example/actions/workflows/test-contracts.yaml/badge.svg" alt="Test Contracts" />
        </a>
        <a href="https://github.com/sergeyklay/provider-pact-example/actions/workflows/test-code.yaml">
            <img src="https://github.com/sergeyklay/provider-pact-example/actions/workflows/test-code.yaml/badge.svg" alt="Test Code" />
        </a>
        <a href="https://github.com/sergeyklay/provider-pact-example/actions/workflows/lint-oas.yaml">
            <img src="https://github.com/sergeyklay/provider-pact-example/actions/workflows/lint-oas.yaml/badge.svg" alt="Lint OpenAPI" />
        </a>
        <a href="https://codecov.io/gh/sergeyklay/provider-pact-example" >
            <img src="https://codecov.io/gh/sergeyklay/provider-pact-example/branch/main/graph/badge.svg?token=2C8W0VZQGN"/>
        </a>
    </p>

.. teaser-begin

Provider API Example is a project that contains a complete Contract Testing solution solution for API,
which can used by client applications.

As an example, this project uses the simple Products API. Here is the
`contract <https://github.com/sergeyklay/provider-pact-example/blob/main/openapi/swagger.yaml>`_
governing the interaction of the client with the product API.

It uses:

* `Pact <https://pact.io>`_
* `pact-python <https://github.com/pact-foundation/pact-python>`_
* `OpenAPI <https://swagger.io>`_
* `Flask <https://flask.palletsprojects.com>`_

.. teaser-end

Requirements
============

* Python >= 3.11
* SQLite3
* Node.js >= 16

How to try it out
=================

Install dependencies and tools
------------------------------

First, install Python dependencies for provider (Products API):

.. code-block:: console

   $ make init
   $ make install


Create provider configuration:

.. code-block:: console

   $ cp .env.example .env

Run database migrations for provider:

.. code-block:: console

   $ make migrate

Add provider seed data to the database:

.. code-block:: console

   $ make seed

Next, install Node.js linters and tools:

.. code-block:: console

   $ npm install

Run API server
--------------

To run API server use the command as follows:

.. code-block:: console

   $ make serve

Run tests
---------

To run unit tests use the command as follows:

.. code-block:: console

   $ make test

To run contract tests use the command as follows:

.. code-block:: console

   $ ./tests/run-pytest.sh

Note that before the contract tests run, you must have deployed the broker,
as well as the contracts (pacts) must be published.

Run lint check
--------------

To run OpenAPI spec checking use the command as follows:

.. code-block:: console

   $ npm run lint

.. -project-information-

Project Information
===================

Provider API Example is released under the `MIT License <https://choosealicense.com/licenses/mit/>`_,
and its code lives at `GitHub <https://github.com/sergeyklay/provider-pact-example>`_.
It’s rigorously tested on Python 3.11+.

If you'd like to contribute to Provider API Example you're most welcome!

.. -support-

Support
=======

Should you have any question, any remark, or if you find a bug, or if there is something
you can't do with the Provider API Example, please
`open an issue <https://github.com/sergeyklay/provider-pact-example/issues>`_.
