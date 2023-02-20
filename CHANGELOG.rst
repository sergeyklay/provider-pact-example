Changelog
=========

This file contains a brief summary of new features and dependency changes or
releases, in reverse chronological order.

.. note::

   Backward incompatible (breaking) changes will only be introduced in major
   versions.


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
* Use thin controller for products API.
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
