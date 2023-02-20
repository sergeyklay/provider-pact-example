# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

NOT_FOUND_RESPONSE = {
        'status': 404,
        'title': 'Not Found',
        'description': 'Invalid resource URI.',
    }


def test_main_page_404(client):
    response = client.get('/')

    assert sorted(NOT_FOUND_RESPONSE.items()) == sorted(response.json.items())
    assert response.status_code == 404


def test_products_empty_database(client):
    response = client.get('/v1/products')

    assert [] == response.json['products']
    assert response.status_code == 200


def test_products_not_found(client):
    response = client.get('/v1/products/99999999')

    assert sorted(NOT_FOUND_RESPONSE.items()) == sorted(response.json.items())
    assert response.status_code == 404
