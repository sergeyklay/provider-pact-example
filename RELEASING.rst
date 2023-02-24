Releasing
=========

1. Increment the version in ``provider/__init__.py``

2. Increment the version in ``package.json`` and ``package-lock.json``

3. Update the ``CHANGELOG.rst`` using:

.. code-block:: console

   $ git log --pretty=format:'  * %h - %s (%an, %ad)' vX.Y.Z..HEAD

4. Add files to git:

.. code-block:: console

   $ git add CHANGELOG.rst package.json package-lock.json
   $ git add provider/__init__.py

5. Commit

.. code-block:: console

   $ git commit -m "Releasing version X.Y.Z"

6. Tag

.. code-block:: console

   $ git tag -a vX.Y.Z -m "Releasing version X.Y.Z"
   $ git push origin main --tags

7. Wait until travis has run and the new tag is available at https://github.com/sergeyklay/contract-testing-example/releases/tag/vX.Y.Z

8. Set the title to ``vX.Y.Z``

9. Save
