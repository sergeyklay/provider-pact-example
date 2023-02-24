# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

from flask import request, Response
from sqlalchemy import or_

from provider.api import api
from provider.app import db
from provider.decorators import json, paginate
from provider.models import Product


@api.route('/products', methods=['POST'])
@json
def new_product():
    product = Product()
    product.import_data(request.json)
    db.session.add(product)
    db.session.commit()

    return {}, 201, {'Location': product.get_url()}


@api.route('/products/<int:product_id>', methods=['GET'])
@json
def get_product(product_id):
    """Get single product.

    Returns a single product and status code 200 if successful,
    otherwise - 404.
    """
    return Product.query.get_or_404(product_id)


@api.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete product.

    Deletes a specified product and returns status code 204 if successful,
    otherwise - 404.
    """
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()

    return Response(status=204)


@api.route('/products', methods=['GET'])
@json
@paginate('products')
def list_products():
    """Get products.

    Returns a list of all products.
    """
    query = Product.query

    category = request.args.get('category')
    if category:
        query = query.filter(Product.category.has(name=category))

    search = request.args.get('q')
    if search:
        query = query.filter(or_(
            Product.title.contains(search),
            Product.description.contains(search),
        ))

    return query
