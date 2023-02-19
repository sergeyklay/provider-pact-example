# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

from flask import abort, json, request, Response

from provider import current_app
from provider.api import api


def _json_dumps(data):
    if current_app.config['DEBUG']:
        return json.dumps(data, indent=2, sort_keys=False, separators=(',', ': '))
    return json.dumps(data, indent=None, sort_keys=False)


def get_products_list():
    with open('products.json') as f:
        return json.loads(f.read())


def save_products_list(data):
    with open('products.json', 'w') as fp:
        fp.write(_json_dumps(data) + '\n')


@api.route('/products', methods=['GET'])
def list_products():
    """Get products.

    Returns a list of all products.
    """
    return Product.query


@api.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    """Get single product.

    Returns a single product.
    """
    # This check is made on purpose to simulate 400 error
    try:
        product_id = int(product_id)
    except ValueError:
        abort(400, description='Invalid product ID data type')
    
    data = get_products_list()
    for product in data:
        if product['id'] == product_id:
            response = current_app.response_class(
                response=_json_dumps(product),
                status=200,
                mimetype='application/json'
            )
            return response

    abort(404, description='Product not found')


@api.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete product.

    Deletes a specific product and returns status code 204 if successful,
    otherwise - 404.
    """
    # This check is made on purpose to simulate 400 error
    try:
        product_id = int(product_id)
    except ValueError:
        abort(400, description='Invalid product ID data type')

    data = get_products_list()
    for i in range(len(data)):
        if data[i]['id'] == product_id:
            del data[i]
            save_products_list(data)
            return Response(status=204)

    abort(404, description='Product not found')
