# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Setup module for Provider."""

import codecs
import re
from os import path

from setuptools import find_packages, setup


def read_file(filepath):
    """Read content from a UTF-8 encoded text file."""
    with codecs.open(filepath, 'rb', 'utf-8') as file_handle:
        return file_handle.read()


PKG_NAME = 'provider'
PKG_DIR = path.abspath(path.dirname(__file__))
META_PATH = path.join(PKG_DIR, PKG_NAME, '__init__.py')
META_CONTENTS = read_file(META_PATH)

# Version regex according to PEP 440
VERSION_REGEX = (r'([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))'
                 r'*((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][0-9]*))'
                 r'?(\.dev(0|[1-9][0-9]*))?')


def long_description():
    """Provide long description for package."""

    def extract_text_between(text, start, end) -> str:
        pattern = f'{re.escape(start)}(.*?){re.escape(end)}'
        result = re.search(pattern, text, re.DOTALL)
        return result.group(1) if result else ''

    def description() -> str:
        readme = path.join(PKG_DIR, 'README.rst')
        if not path.isfile(readme):
            return ''

        text = read_file(readme)
        return extract_text_between(
            text,
            '.. teaser-begin',
            '.. teaser-end'
        ).strip()

    def changes() -> str:
        changelog = path.join(PKG_DIR, 'CHANGELOG.rst')
        if not path.isfile(changelog):
            return ''

        pattern = (fr'({VERSION_REGEX} \(.*?\)\r?\n.*?)'
                   r'\r?\n\r?\n\r?\n----\r?\n\r?\n\r?\n')
        result = re.search(pattern, read_file(changelog), re.S)

        return result.group(1) if result else ''

    try:
        title = f"{PKG_NAME}: {find_meta('description')}"
        head = '=' * (len(title) - 1)

        contents = (
            head,
            format(title.strip(' .')),
            head,
            '',
            description(),
            '',
            'Release Information',
            '===================\n',
            changes(),
            '',
            f"`Full changelog <{find_meta('url')}/blob/main/CHANGELOG.rst>`_.",
            '',
            read_file(path.join(PKG_DIR, 'SECURITY.rst')),
            '',
            read_file(path.join(PKG_DIR, 'AUTHORS.rst')),
        )
        return '\n'.join(contents)
    except (RuntimeError, FileNotFoundError) as read_error:
        message = 'Long description could not be read from README.rst'
        raise RuntimeError(f'{message}: {read_error}') from read_error


def is_canonical_version(version):
    """Check if a version string is in the canonical format of PEP 440."""
    pattern = fr'^{VERSION_REGEX}$'
    return re.match(pattern, version) is not None


def find_meta(meta):
    """Extract __*meta*__ from META_CONTENTS."""
    meta_match = re.search(
        fr"^__{meta}__\s+=\s+['\"]([^'\"]*)['\"]",
        META_CONTENTS,
        re.M
    )

    if meta_match:
        return meta_match.group(1)
    raise RuntimeError(
        f'Unable to find __{meta}__ string in package meta file')


def get_version_string():
    """Return package version as listed in `__version__` in meta file."""
    # Parse version string
    version_string = find_meta('version')

    # Check validity
    if not is_canonical_version(version_string):
        message = (
            f'The detected version string "{version_string}" is not in '
            'canonical format as defined in PEP 440.')
        raise ValueError(message)

    return version_string


# What does this project relate to.
KEYWORDS = [
    'api',
    'contracts',
    'api-testing',
    'contract-testing',
    'contract-test',
    'pact',
    'pact-provider',
    'openapi3',
    'openapi',
]

# Classifiers: available ones listed at https://pypi.org/classifiers
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',

    'Environment :: Console',

    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',

    'Natural Language :: English',

    'License :: OSI Approved :: MIT',
    'Operating System :: OS Independent',

    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3 :: Only',
]

# Dependencies that are downloaded by pip on installation and why.
INSTALL_REQUIRES = [
    'Flask-Migrate>=4.0.0',  # SQLAlchemy database migrations for Flask app
    'Flask-SQLAlchemy>=3.0.3',  # Adds SQLAlchemy support to Flask application
    'Flask>=2.2.2',  # Our framework for building API
    'SQLAlchemy>=2.0.0',  # Database Abstraction Library
    'Werkzeug>=2.2.0',  # Read key-value pairs from a .env file
    'alembic>=1.9.0',  # A database migration tool for SQLAlchemy
    'flask-smorest>=0.40.0',  # Flask/Marshmallow-based REST API framework
    'marshmallow>=3.19.0',  # Complex data (de)serialization
    'python-dotenv>=0.21.0',  # Read key-value pairs from a .env file
]

DEPENDENCY_LINKS = []

# List additional groups of dependencies here (e.g. testing dependencies).
# You can install these using the following syntax, for example:
#
#    $ pip install -e .[testing,docs,develop]
#
EXTRAS_REQUIRE = {
    # Dependencies that are required to run tests
    'testing': [
        'Faker>=17.0.0',  # Generates fake data
        'coverage[toml]>=6.0',  # Code coverage measurement for Python
        'factory_boy>=3.2.0',  # A versatile test fixtures replacement
        'flake8-blind-except>=0.2.0',  # Checks for blind except: statements
        'flake8-import-order>=0.18.1',  # Checks the ordering of imports
        'flake8>=6.0.0',  # The modular source code checker
        'pact-python>=1.7.0',  # Create and verify consumer driven contracts
        'pylint>=2.6.2',  # Python code static checker
        'pytest>=6.2.4',  # Our tests framework
    ],
    'docs': [
    ],
}

# Dependencies that are required to develop package
DEVELOP_REQUIRE = []

EXTRAS_REQUIRE['develop'] = \
    DEVELOP_REQUIRE + \
    EXTRAS_REQUIRE['testing'] + \
    EXTRAS_REQUIRE['docs']

# Project's URLs
PROJECT_URLS = {
    'Documentation': find_meta('url'),
    'Changelog': f"{find_meta('url')}/blob/main/CHANGELOG.rst",
    'Bug Tracker': f"{find_meta('url')}/issues",
    'Source Code': find_meta('url'),
}

if __name__ == '__main__':
    setup(
        name=PKG_NAME,
        version=get_version_string(),
        author=find_meta('author'),
        author_email=find_meta('author_email'),
        maintainer=find_meta('author'),
        maintainer_email=find_meta('author_email'),
        license=find_meta('license'),
        description=find_meta('description'),
        long_description=long_description(),
        long_description_content_type='text/x-rst',
        keywords=KEYWORDS,
        url=find_meta('url'),
        project_urls=PROJECT_URLS,
        classifiers=CLASSIFIERS,
        packages=find_packages(exclude=['tests.*', 'tests']),
        platforms='any',
        include_package_data=True,
        zip_safe=False,
        python_requires='>=3.11, <4',
        install_requires=INSTALL_REQUIRES,
        dependency_links=DEPENDENCY_LINKS,
        extras_require=EXTRAS_REQUIRE,
    )
