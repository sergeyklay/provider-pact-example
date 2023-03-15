# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Various pact tools to working with contracts verification."""

from sqlalchemy import delete

from provider.app import db
from provider.models import Category, Brand, Product
from .factories import CategoryFactory, BrandFactory, ProductFactory


class StateManager:
    """Provider State Setup"""

    def __init__(self, **kwargs):
        self.consumer: str = kwargs.get('consumer', '')
        self.state: str = kwargs.get('state', '')
        self.states: list = kwargs.get('states', [])
        self.params: dict = kwargs.get('params', {})

        self._STATE_SETUP_MAPPING = {
            'there is a product with ID 1': self._create_product,
            'there is no product with ID 7777': self._delete_product,
            'there are no products': self._delete_all_products,
            'there are few products': self._create_few_products,
            'there are no products in category #2': self._delete_prod_category,
            'there are few products in category #2': self._create_cat_products,
            'there is category #1 and brand #1': self._create_cat_brand_only,
        }

    def change_provider_state(self):
        if self.state in self._STATE_SETUP_MAPPING:
            self._STATE_SETUP_MAPPING[self.state]()

    def _create_product(self):
        self._delete_all_products()
        ProductFactory(id=1, name='product0')

    def _create_few_products(self):
        self._delete_all_products()
        for i in range(1, 4):
            ProductFactory(id=i)

    def _create_cat_products(self):
        self._delete_all_products()
        self._delete_all_categories()

        category = CategoryFactory(id=2)
        for i in range(1, 3):
            ProductFactory(id=i, category=category)

    def _create_cat_brand_only(self):
        self._delete_all()

        CategoryFactory(id=1)
        BrandFactory(id=1)

    def _delete_product(self):
        product = Product.query.get(7777)
        if product is not None:
            db.session.delete(product)
            db.session.commit()

    def _delete_all_products(self):
        db.session.query(Product).delete()
        db.session.commit()

    def _delete_all_categories(self):
        db.session.query(Category).delete()
        db.session.commit()

    def _delete_all_brands(self):
        db.session.query(Brand).delete()
        db.session.commit()

    def _delete_all(self):
        self._delete_all_products()
        self._delete_all_brands()
        self._delete_all_categories()

    def _delete_prod_category(self):
        db.session.execute(
            delete(Product).where(Product.category.has(id=2))
        )
        db.session.commit()
