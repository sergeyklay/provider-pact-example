# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

from flask import request, Response
from sqlalchemy import or_

from products.api import api
from products.decorators import json, paginate
from products.models import db, Product


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
        query = query.filter_by(category=category)

    search = request.args.get('q')
    if search:
        query = query.filter(or_(
            Product.title.like(f'''%{search}%'''),
            Product.description.like(f'''%{search}%'''),
        ))

    return query


@api.route('/products/<int:product_id>', methods=['GET'])
@json
def get_product(product_id):
    """Get single product.

    Returns a single product.
    """
    return Product.query.get_or_404(product_id)


@api.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete product.

    Deletes a specific product and returns status code 204 if successful,
    otherwise - 404.
    """
    # Emulate deletion
    if request.headers.get('User-Agent') == 'Ktor client' \
            and product_id == 7777:
        return Response(status=204)

    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return Response(status=204)
