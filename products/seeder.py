# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Seed the database with fake data."""

import random

from faker import Faker
from faker.providers import company, lorem, python
from sqlalchemy.exc import IntegrityError

from products.app import db
from .models import Category, Product


def seed_products():
    """Add seed product data to the database."""
    db.create_all()

    fake = Faker()

    fake.add_provider(company)
    fake.add_provider(lorem)
    fake.add_provider(python)

    categories = []
    for _ in range(10):
        try:
            category = Category(name=' '.join(fake.words(nb=1)).lower())
            category.save()
        except IntegrityError:
            category = Category(name=' '.join(fake.words(nb=1)).lower())
            category.save()
        categories.append(category)

    for _ in range(1000):
        price = fake.pyfloat(
            left_digits=3,
            right_digits=2,
            min_value=1.0,
            max_value=999.99,
        )

        product = Product(
            title=' '.join(fake.words(nb=5)).capitalize(),
            description=fake.sentence(nb_words=10),
            price=price,
            discount=fake.pyfloat(
                left_digits=3,
                right_digits=2,
                min_value=0.0,
                max_value=price,
            ),
            rating=fake.pyfloat(
                left_digits=1,
                right_digits=2,
                min_value=0.0,
                max_value=5.0,
            ),
            stock=fake.pyint(min_value=0, max_value=999),
            brand=fake.company(),
            category=random.choice(categories),
        )
        product.save()
