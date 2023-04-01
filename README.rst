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
            <img src="https://codecov.io/gh/sergeyklay/provider-pact-example/branch/main/graph/badge.svg?token=2C8W0VZQGN" alt="Coverage Status"/>
        </a>
    </p>

.. teaser-begin

This is a Python application for explanation of Contract Testing based on
`Pact <https://docs.pact.io>`_.

Here you can find out how to use Pact using the Python language. You can find
more of an overview on Pact in the `Pact Introduction <https://docs.pact.io/>`_.

This project uses:

* `Pact <https://pact.io>`_, a code-first tool for testing HTTP and message
  integrations using contract tests
* `pact-python <https://github.com/pact-foundation/pact-python>`_, to create
  and verify consumer driven contracts
* `OpenAPI <https://swagger.io>`_, to describe the Products API
* `Flask <https://flask.palletsprojects.com>`_, a micro web framework for
  building API

.. teaser-end

.. image:: https://raw.githubusercontent.com/sergeyklay/provider-pact-example/main/cdc-example.png
  :alt: Interaction diagram

Provider
========

Provider API Example is a sample Flask application that expose endpoints with
REST standard. As an example, this project uses the simple Products API. Here
is the
`OpenAPI spec <https://github.com/sergeyklay/provider-pact-example/blob/main/openapi/swagger.yaml>`_
describes the interaction of clients with the provider.

Consumer
========

For the purity of the experiment, the consumer is implemented as a separate
project and can be found at
`the following repo <https://github.com/sergeyklay/consumer-pact-example>`_.

Pact
====

Sample contracts (pacts) are located here:
https://github.com/sergeyklay/consumer-pact-example/tree/main/tests/pacts

Getting Started
===============

Prerequisites
-------------

What kind of things you need to install on your workstation to start:

* Python >= 3.11
* SQLite3
* Node.js >= 16

Installing
----------

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

To verify contracts (pacts) use the command as follows:

.. code-block:: console

   $ ./tests/run-pytest.sh

Note that before the contracts verification, you must have deployed the broker,
as well as the contracts must be published.

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

Should you have any question, any remark, or if you find a bug, or if there is
something you can't do with the Provider API Example, please
`open an issue <https://github.com/sergeyklay/provider-pact-example/issues>`_.
