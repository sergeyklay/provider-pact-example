# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

from flask import Response
from flask.views import MethodView
from flask_smorest import Page
from sqlalchemy import or_

from provider.api import api
from provider.app import db
from provider.models import Brand, Category, Product
from .schemas import ProductQueryArgsSchema, ProductSchema


class CursorPage(Page):
    @property
    def item_count(self):
        return self.collection.count()


@api.route('/products')
@api.etag
class Products(MethodView):

    @api.arguments(ProductQueryArgsSchema, location='query')
    @api.response(200, ProductSchema(many=True))
    @api.paginate(CursorPage)
    def get(self, args):
        """List products."""
        query = Product.query
        category_id = args.get('cid')
        if category_id is not None:
            query = query.filter(Product.category.has(id=category_id))

        brand_id = args.get('bid')
        if brand_id is not None:
            query = query.filter(Product.brand.has(id=brand_id))

        search = args.get('q')
        if search is not None and search:
            query = query.filter(or_(
                Product.title.contains(search),
                Product.description.contains(search),
            ))

        return query

    @api.arguments(ProductSchema)
    @api.response(201, ProductSchema)
    @api.alt_response(400, description='Validation error')
    def post(self, data: dict):
        """Add a new product."""
        # Validate and deserialize request data
        product_schema = ProductSchema()
        data = product_schema.load(data)

        brand = Brand.query.get(data.pop('brand_id'))
        category = Category.query.get(data.pop('category_id'))

        # TODO: sqlalchemy.exc.IntegrityError
        # Create product
        product = Product(**data, brand=brand, category=category)

        # Save product to database
        db.session.add(product)
        db.session.commit()

        headers = {'Location': product.get_url()}

        return product, 201, headers


@api.route('/products/<int:product_id>')
@api.etag
class ProductsById(MethodView):
    @api.response(200, ProductSchema)
    @api.alt_response(404, description='Product not found')
    def get(self, product_id: int):
        """Get single product.

        Returns a single product and status code 200 if successful,
        otherwise - 404.
        """
        return Product.query.get_or_404(product_id)

    @api.response(204)
    @api.alt_response(404, description='Product not found')
    @api.alt_response(428, description='Precondition failed')
    def delete(self, product_id: int):
        """Delete product.

        Deletes a specified product and returns status code 204 if successful,
        otherwise - 404.
        """
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()

        return Response(status=204)
