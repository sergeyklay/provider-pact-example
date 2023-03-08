# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Module for Pagination API testing."""


def test_paginate_empty_db(client):
    rv = client.get('/v2/products')

    # TODO: check headers, X-Pagination, Etag, etc
    assert rv.status_code == 200
    assert rv.json == []


def test_paginate_empty_db_fist_page(client):
    rv = client.get('/v2/products?page=1')

    # TODO: check headers, X-Pagination, Etag, etc
    assert rv.status_code == 200
    assert rv.json == []


def test_paginate_links_returns_extra_keys(client):
    rv = client.get('/v2/products?a=b&c=d&e=f')

    # TODO: check headers, X-Pagination, Etag, etc
    assert rv.status_code == 200
    assert rv.json == []


def test_paginate_0_page(client):
    rv = client.get('/v2/products?page=0')

    expected = [
        ('code', 422),
        ('errors', {
            'query': {
                'page': ['Must be greater than or equal to 1.']
            },
        }),
        ('status', 'Unprocessable Entity'),
    ]

    assert sorted(expected) == sorted(rv.json.items())
    assert rv.status_code == 422
