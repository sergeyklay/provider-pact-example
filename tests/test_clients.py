# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

def test_main_page_404(client):
    """See error when request to main page."""
    response = client.get('/')
    expected = {
        'status': 404,
        'title': 'Not Found',
        'description': 'Invalid resource URI.',
    }

    assert sorted(expected.items()) == sorted(response.json.items())
    assert response.status_code == 404


def test_products_empty_database(client):
    response = client.get('/v1/products')
    assert response.status_code == 200
