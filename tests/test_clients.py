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


def test_delete_product_empty_database(client):
    response = client.delete('/v1/products/1')

    assert sorted(NOT_FOUND_RESPONSE.items()) == sorted(response.json.items())
    assert response.status_code == 404


def test_delete_special_product_empty_database(client):
    response = client.delete('/v1/products/7777')

    assert sorted(NOT_FOUND_RESPONSE.items()) == sorted(response.json.items())
    assert response.status_code == 404

    client.environ_base['HTTP_USER_AGENT'] = 'Ktor client'
    response = client.delete('/v1/products/7777')
    assert response.status_code == 204


def test_products_with_query_params_empty_database(client):
    response = client.get('/v1/products?expanded=1&category=laptops&q=')

    assert [] == response.json['products']
    assert response.status_code == 200


def test_products_not_found(client):
    response = client.get('/v1/products/99999999')

    assert sorted(NOT_FOUND_RESPONSE.items()) == sorted(response.json.items())
    assert response.status_code == 404
