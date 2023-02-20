.. raw:: html

    <h1 align="center">Specmatic Testing Example</h1>
    <p align="center">
        <a href="https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/contracts.yaml">
            <img src="https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/contracts.yaml/badge.svg" alt="Check Contracts" />
        </a>
        <a href="https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/versions.yaml">
            <img src="https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/versions.yaml/badge.svg" alt="Validate Action" />
        </a>
        <a href="https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/lint.yaml">
            <img src="https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/lint.yaml/badge.svg" alt="Lint OpenAPI" />
        </a>
    </p>

.. teaser-begin

Specmatic Testing Example is a project that contains a complete Contract Testing solution solution for API,
which can used by client applications

As an example, this project uses the simple products API. Here is the
`contract <https://github.com/sergeyklay/specmatic-testing-example/blob/main/contracts/documentation.yaml>`_
governing the interaction of the client with the product API.

It uses:

* `Specmatic <https://specmatic.in>`_
* `OpenAPI <https://swagger.io>`_
* `Flask <https://flask.palletsprojects.com>`_

.. teaser-end

Requirements
============

* Python 3.8 >= 3.8
* SQLite3
* Node.js >= 16

How to try it out
=================

Install dependencies and tools
------------------------------

First, install Python dependencies:

.. code-block:: console

   $ # make init
   $ python3 -m pip install -r requirements.txt


Run database migrations

.. code-block:: console

   $ flask --app runner:app db upgrade

Add seed data to the database

.. code-block:: console

   $ flask --app runner:app seed

Next, install Node.js linters and tools:

.. code-block:: console

   $ npm install

Finally, install [specmatic](https://specmatic.in/download/latest.html).

Run API server
--------------

To run API server use the command as follows:

.. code-block:: console

   $ flask --app runner:app run

Run the contract tests
----------------------

To run contract tests use the command as follows:

.. code-block:: console

   $ java -jar specmatic.jar test --testBaseURL=http://127.0.0.1:5000

Run lint check
--------------

To run code style checking use the command as follows:

.. code-block:: console

   $ npm run lint

.. -project-information-

Project Information
===================

Specmatic Testing Example is released under the `MIT License <https://choosealicense.com/licenses/mit/>`_,
and its code lives at `GitHub <https://github.com/sergeyklay/specmatic-testing-example>`_.
It’s rigorously tested on Python 3.11+.

If you'd like to contribute to Gstore you're most welcome!

.. -support-

Support
=======

Should you have any question, any remark, or if you find a bug, or if there is something
you can't do with the Specmatic Testing Example, please
`open an issue <https://github.com/sergeyklay/specmatic-testing-example/issues>`_.