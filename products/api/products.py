# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

from flask import request
from sqlalchemy import or_

from products.api import api
from products.decorators import json, paginate
from products.models import Product


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
