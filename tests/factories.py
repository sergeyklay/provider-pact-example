# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Providing various factories for testing purposes."""

import random

import factory
from faker import Factory

from provider import models
from provider.app import db

faker = Factory.create()


class BrandFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.Brand
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: 'brand%d' % n)


class CategoryFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.Category
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: 'category%d' % n)


class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.Product
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    title = factory.Sequence(lambda n: 'product%d' % n)
    description = factory.Sequence(lambda n: 'description%d' % n)
    price = factory.LazyFunction(lambda: round(random.uniform(1.0, 500.0), 2))
    discount = factory.LazyFunction(
        lambda: round(random.uniform(1.0, 100.0), 2))
    rating = factory.LazyFunction(lambda: round(random.uniform(1.0, 5.0), 2))
    stock = factory.Iterator(range(10, 1000))
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
