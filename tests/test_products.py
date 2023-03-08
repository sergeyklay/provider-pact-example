# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Module for Product API testing."""

from urllib.parse import urlsplit

from .factories import BrandFactory, CategoryFactory, ProductFactory

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
    response = client.get('/v2/products')

    assert [] == response.json['products']
    assert response.status_code == 200


def test_delete_product_empty_database(client):
    response = client.delete('/v2/products/1')

    assert sorted(NOT_FOUND_RESPONSE.items()) == sorted(response.json.items())
    assert response.status_code == 404


def test_products_with_query_params_empty_database(client):
    response = client.get('/v2/products?expanded=1&category=laptops&q=')

    assert [] == response.json['products']
    assert response.status_code == 200


def test_products_not_found(client):
    response = client.get('/v2/products/99999999')

    assert sorted(NOT_FOUND_RESPONSE.items()) == sorted(response.json.items())
    assert response.status_code == 404


def test_create_product(client):
    brand = BrandFactory()
    category = CategoryFactory()

    data = dict(
        title='Test',
        description='Description',
        discount=0.0,
        price=0.0,
        rating=0.0,
        stock=0,
        brand_id=brand.id,
        category_id=category.id
    )

    # add a product
    rv = client.post('/v2/products', json=data)

    assert rv.json == {}
    assert rv.status_code == 201
    assert 'Location' in rv.headers

    assert urlsplit(rv.headers['Location']).path == '/v2/products/1'

    # get product
    rv = client.get(urlsplit(rv.headers['Location']).path)
    assert rv.status_code == 200
    assert rv.json['brand'] == brand.name

    # get list of products
    rv = client.get('/v2/products?expanded=1')

    assert rv.status_code == 200
    assert len(rv.json) == 3
    assert len(rv.json['products']) == 1
    assert rv.json['products'][0]['category'] == category.name


def test_product_invalid_format(client):
    brand = BrandFactory()
    category = CategoryFactory()

    data = dict(
        title='Test',
        description='Description',
        discount=0.0,
        price=0.0,
        rating=0.0,
        stock=0,
        brand_id=brand.id,
        category_id=category.id
    )

    # not a JSON
    rv = client.post('/v2/products', data=data)
    assert rv.status_code == 400


def test_product_integrity_error(client):
    brand = BrandFactory()
    category = CategoryFactory()
    product = ProductFactory(brand=brand, category=category)

    data = dict(
        title=product.title,
        description='Description',
        discount=0.0,
        price=0.0,
        rating=0.0,
        stock=0,
        brand_id=brand.id,
        category_id=category.id
    )

    # integrity error (unique title)
    rv = client.post('/v2/products', json=data)
    assert rv.status_code == 400


def test_product_missing_data(client):
    brand = BrandFactory()
    category = CategoryFactory()

    data = dict(
        brand_id=brand.id,
        category_id=category.id
    )

    # missing data
    rv = client.post('/v2/products', json=data)
    assert rv.status_code == 400
