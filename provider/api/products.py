# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

from flask import abort, json, request, Response

from provider import current_app
from provider.api import api

def get_products_list():
    with open('products.json') as f:
        return json.loads(f.read())


@api.route('/products', methods=['GET'])
def list():
    data = get_products_list()
    args = request.args

    category = args.get('category')
    q = args.get('q')
    
    products = []
    for p in data:
        if q is not None and len(q.strip()) > 0:
            descr = p['description'].lower()
            title = p['title'].lower()
            brand = p['brand'].lower()
            if q.lower() not in descr and q.lower() not in title and q.lower() not in brand:
                continue
        if category is not None and len(category.strip()) > 0:
            if p['category'].lower() != category.lower():
                continue
        products.append(p)

    response = current_app.response_class(
        response=json.dumps(products),
        status=200,
        mimetype='application/json'
    )
    return response


@api.route('/products/<id>', methods=['GET'])
def get(id):
    # This check is made on purpose to simulate 400 error
    try:
        id = int(id)
    except ValueError:
        abort(400, description='Invalid product ID data type')
    
    data = get_products_list()
    for product in data:
        if product['id'] == id:
            response = current_app.response_class(
                response=json.dumps(product),
                status=200,
                mimetype='application/json'
            )
            return response

    abort(404, description='Product not found')
