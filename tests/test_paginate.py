# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Module for Pagination API testing."""

from urllib.parse import urlsplit


def test_paginate_empty_db(client):
    rv = client.get('/v2/products')

    assert rv.status_code == 200

    assert rv.json['pagination']['total'] == 0
    assert rv.json['pagination']['page'] == 1
    assert rv.json['pagination']['pages'] == 1
    assert rv.json['pagination']['per_page'] == 10

    assert rv.json['links']['prev'] is None
    assert rv.json['links']['next'] is None

    url = urlsplit(rv.json['links']['first'])
    assert '?'.join([url.path, url.query]) == '/v2/products?page=1&per_page=10'

    url = urlsplit(rv.json['links']['last'])
    assert '?'.join([url.path, url.query]) == '/v2/products?page=1&per_page=10'


def test_paginate_empty_db_fist_page(client):
    rv = client.get('/v2/products?page=1')

    assert rv.status_code == 200

    assert rv.json['pagination']['total'] == 0
    assert rv.json['pagination']['page'] == 1
    assert rv.json['pagination']['pages'] == 1
    assert rv.json['pagination']['per_page'] == 10

    assert rv.json['links']['prev'] is None
    assert rv.json['links']['next'] is None

    url = urlsplit(rv.json['links']['first'])
    assert '?'.join([url.path, url.query]) == '/v2/products?page=1&per_page=10'

    url = urlsplit(rv.json['links']['last'])
    assert '?'.join([url.path, url.query]) == '/v2/products?page=1&per_page=10'


def test_paginate_links_returns_extra_keys(client):
    rv = client.get('/v2/products?a=b&c=d&e=f')

    assert rv.status_code == 200

    assert rv.json['links']['prev'] is None
    assert rv.json['links']['next'] is None

    url = urlsplit(rv.json['links']['first'])
    assert '?'.join([url.path, url.query]) == (
        '/v2/products?page=1&per_page=10&a=b&c=d&e=f'
    )

    url = urlsplit(rv.json['links']['last'])
    assert '?'.join([url.path, url.query]) == (
        '/v2/products?page=1&per_page=10&a=b&c=d&e=f'
    )


def test_paginate_0_page(client):
    rv = client.get('/v2/products?page=0')

    expected = {
        'status': 400,
        'title': 'Bad Request',
        'description': ("The 'page' parameter cannot be less than 1, "
                        'received: 0.'),
    }

    assert sorted(expected.items()) == sorted(rv.json.items())
    assert rv.status_code == 400
