Changelog
=========

This file contains a brief summary of new features and dependency changes or
releases, in reverse chronological order.


2.0.0 (2023-02-27)
------------------

Features
^^^^^^^^

* Migrate contract testing to Pact.


Bug Fixes
^^^^^^^^^

* Fixed database seeder to not try to create tables twice.


Improved Documentation
^^^^^^^^^^^^^^^^^^^^^^

* Improved project documentation.


Trivial/Internal Changes
^^^^^^^^^^^^^^^^^^^^^^^^

* Rework Contract Tests workflow.


----


1.8.0 (2023-02-26)
------------------

Features
^^^^^^^^

* Provided ability to create products.


Breaking Changes
^^^^^^^^^^^^^^^^

* Remove no longer needed ``self_url`` Product attribute.
* Renamed project name from ``Specmatic Testing Example`` to
  ``Contract Testing Example``.
* Renamed OpenAPI directory and filename to reflect its purpose from
  ``contracts`` to ``openapi``.
* Renamed Python package from ``products`` to ``provider``.


Trivial/Internal Changes
^^^^^^^^^^^^^^^^^^^^^^^^

* Amended tests.
* Minor documentation improvements and fixes.
* Refactor ``redocly`` linter configuration.
* Remove no longer needed ``spectral`` linter.
* Simplify ``setup.py`` to provide long description.
* Bump ``markdown-it-py`` from 2.1.0 to 2.2.0.
* Bump ``python-dotenv`` from 0.21.1 to 1.0.0.
* Bump ``faker`` from 17.0.0 to 17.1.0.
* Bump ``actions/labeler`` from 4.0.2 to 4.1.0.


----


1.7.0 (2023-02-22)
------------------

Features
^^^^^^^^

* Rework the main application entry point to provide more options for launching
  the application.


Improvements
^^^^^^^^^^^^

* Improve OpenAPI spec documentation.
* Amend contract tests for product API.


Bug Fixes
^^^^^^^^^

* Fixed pagination response to not offer 0 page.
* Fixed response code for 400 error.


Breaking Changes
^^^^^^^^^^^^^^^^

* Separate pagination ``links`` in responses to a separate response attribute.
* Rename ``pages`` response attribute to ``pagination``.


Trivial/Internal Changes
^^^^^^^^^^^^^^^^^^^^^^^^

* Separate Python code linting into a separate workflow.
* Extract database seeder into a separate module.
* Move ``db`` definition to ``app`` module.
* Use SQLAlchemy 2.x way to declare ORM models.
* Separate Categories into a separate ORM model.
* Separate Brands into a separate ORM model.


----


1.6.0 (2023-02-20)
------------------

Features
^^^^^^^^

* Provided ability to paginate responses.


Improvements
^^^^^^^^^^^^

* Introduced unit tests for products API.


Bug Fixes
^^^^^^^^^

* Returned ability to filter products by category.
* Returned ability to filter products fuzzy search.


Breaking Changes
^^^^^^^^^^^^^^^^

* Renamed Python package from ``provider`` to ``products``.


Trivial/Internal Changes
^^^^^^^^^^^^^^^^^^^^^^^^

* Removed abandoned ``openapi-enforcer`` from the list of used linters.
* Provided python package manifest.
* Added python code linters (``pylint``, ``flake8``) to CI pipeline.


----


1.5.0 (2023-02-20)
------------------

Features
^^^^^^^^

* Store products in DB instead of JSON file.
* Generate an ``ETag`` header for API routes.
* Provide JSON decorator for API calls.
* Add ``self_url`` attribute to product response.


Improvements
^^^^^^^^^^^^

* Set ``minLength`` and ``maxLength`` for OpenAPI string values.
* Use thin view for products API.
* Redesign error responses.


Improved Documentation
^^^^^^^^^^^^^^^^^^^^^^

* Improved project documentation.


Trivial/Internal Changes
^^^^^^^^^^^^^^^^^^^^^^^^

* Used matrix contract testing at CI phase.
* Reduce repetitive code in OpenAPI spec.
* Enable ``spectral`` linter at CI phase.
* Bumped ``werkzeug`` from 2.2.2 to 2.2.3.
* Bumped ``flask`` from 2.2.2 to 2.2.3


----


1.4.0 (2023-02-13)
------------------

Features
^^^^^^^^

* Provided ability to delete products using ``DELETE`` http method.
* Added API backward compatibility check for CI phase.
* Provide all-in-one build/test/run tool with help of Makefile.


Improved Documentation
^^^^^^^^^^^^^^^^^^^^^^

* Improved project documentation.


Trivial/Internal Changes
^^^^^^^^^^^^^^^^^^^^^^^^

* Used ``spectral`` linter at CI phase to validate  OpenAPI spec.
* Bumped ``tj-actions/changed-files`` from 34 to 35.


----


1.3.0 (2023-02-07)
------------------

Breaking Changes
^^^^^^^^^^^^^^^^

* Migrated to modular application structure with help of Flask Blueprints.


----


1.2.0 (2023-02-06)
------------------

Features
^^^^^^^^

* Added examples to OpenAPI spec.
* Added description to operations.


Improvements
^^^^^^^^^^^^

* Refactor OpenAPI spec by merging objects.


Bug Fixes
^^^^^^^^^

* Deleted useless ``Accept`` header from OpenAPI spec.
* Removed deprecated ``allowEmptyValue`` property from OpenAPI spec.


Trivial/Internal Changes
^^^^^^^^^^^^^^^^^^^^^^^^

* Used ``redocly`` and ``openapi-enforcer`` linters at CI phase
  to validate  OpenAPI spec.


----


1.1.0 (2020-02-05)
------------------

Features
^^^^^^^^

* Added ``category`` filter support for product list.
* Added ability to use fuzzy search when getting products.


Breaking Changes
^^^^^^^^^^^^^^^^

* Refactor project structure.


----


1.0.0 (2023-02-04)
------------------

* Initial release.
