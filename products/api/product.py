# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

from flask import Response

from products.api import api
from products.app import db
from products.decorators import json
from products.models import Product


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
