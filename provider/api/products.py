# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Module for serving API request for products."""

from flask import Response
from flask.views import MethodView
from flask_smorest import abort, Page
from sqlalchemy import or_

from provider.api import api
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
                Product.name.contains(search),
                Product.description.contains(search),
            ))

        return query

    @api.arguments(ProductSchema)
    @api.response(201, ProductSchema)
    @api.alt_response(400, description='Bad Request')
    @api.alt_response(422, description='Unprocessable Entity')
    def post(self, data: dict):
        """Add a new product."""
        # Validate and deserialize request data
        product_schema = ProductSchema()
        data = product_schema.load(data)

        if Product.query.filter(Product.name == data['name']).first():
            abort(422, message='Product with this name already exists')

        brand = Brand.get_or_404(data.pop('brand_id'))
        category = Category.get_or_404(data.pop('category_id'))

        product = Product.create(**data, brand=brand, category=category)
        product.save()

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
        product = Product.get_or_404(product_id)
        headers = {
            'Last-Modified': product.last_modified(),
        }

        return product, 200, headers

    @api.response(204)
    @api.alt_response(404, description='Product not found')
    @api.alt_response(412, description='Precondition Failed')
    @api.alt_response(428, description='Precondition Required')
    def delete(self, product_id: int):
        """Delete product.

        Deletes a specified product and returns status code 204 if successful,
        otherwise - 404.
        """
        product = Product.get_or_404(product_id)
        api.check_etag(product, ProductSchema)
        product.delete()

        return Response(status=204)
