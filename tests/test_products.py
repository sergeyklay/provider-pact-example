# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

from urllib.parse import urlsplit

from provider.app import db
from provider.models import Brand, Category

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


def test_products_with_query_params_empty_database(client):
    response = client.get('/v1/products?expanded=1&category=laptops&q=')

    assert [] == response.json['products']
    assert response.status_code == 200


def test_products_not_found(client):
    response = client.get('/v1/products/99999999')

    assert sorted(NOT_FOUND_RESPONSE.items()) == sorted(response.json.items())
    assert response.status_code == 404


def test_create_product(client):
    brand = Brand(name='Acme')
    category = Category(name='Test')

    db.session.add(brand)
    db.session.add(category)
    db.session.commit()

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
    rv = client.post('/v1/products', json=data)

    assert rv.json == {}
    assert rv.status_code == 201
    assert 'Location' in rv.headers

    assert urlsplit(rv.headers['Location']).path == '/v1/products/1'

    # get product
    rv = client.get(urlsplit(rv.headers['Location']).path)
    assert rv.status_code == 200
    assert rv.json['brand'] == 'Acme'

    # get list of products
    rv = client.get('/v1/products?expanded=1')

    assert rv.status_code == 200
    assert len(rv.json) == 3
    assert len(rv.json['products']) == 1
    assert rv.json['products'][0]['category'] == 'Test'


def test_product_integrity_error(client):
    brand = Brand(name='test_product_integrity_error')
    category = Category(name=brand.name)

    db.session.add(brand)
    db.session.add(category)
    db.session.commit()

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
    rv = client.post('/v1/products', data=data)
    assert rv.status_code == 400

    # create product
    rv = client.post('/v1/products', json=data)
    assert rv.status_code == 201

    # integrity error
    rv = client.post('/v1/products', json=data)
    assert rv.status_code == 400


def test_product_missing_data(client):
    brand = Brand(name='test_product_missing_data')
    category = Category(name=brand.name)

    db.session.add(brand)
    db.session.add(category)
    db.session.commit()

    data = dict(
        brand_id=brand.id,
        category_id=category.id
    )

    # missing data
    rv = client.post('/v1/products', json=data)
    assert rv.status_code == 400
