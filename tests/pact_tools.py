# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Various pact tools to working with contracts verification."""

from provider.app import db
from provider.models import Product
from .factories import ProductFactory


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
        }

    def change_provider_state(self):
        if self.state in self._STATE_SETUP_MAPPING:
            self._STATE_SETUP_MAPPING[self.state]()

    def _create_product(self):
        ProductFactory(id=1)

    def _delete_product(self):
        product = Product.query.get(7777)
        if product is not None:
            db.session.delete(product)
            db.session.commit()
