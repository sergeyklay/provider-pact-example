# This file is part of the Contract Testing Example.
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
from .models import Brand, Category, Product


def seed_products():
    """Add seed product data to the database."""
    db.create_all()

    fake = Faker()

    fake.add_provider(company)
    fake.add_provider(lorem)
    fake.add_provider(python)

    brands = []
    batch_size = 10
    while len(brands) < batch_size:
        try:
            brand = Brand(name=fake.company())
            db.session.add(brand)
            db.session.commit()
            brands.append(brand)
        except IntegrityError:
            db.session.rollback()

    categories = []
    batch_size = 10
    while len(categories) < batch_size:
        try:
            category = Category(name=''.join(fake.words(nb=1)).lower())
            db.session.add(category)
            db.session.commit()
            categories.append(category)
        except IntegrityError:
            db.session.rollback()

    batch_size = 1000
    created = 0
    while created < batch_size:
        try:
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
                brand=random.choice(brands),
                category=random.choice(categories),
            )
            db.session.add(product)
            db.session.commit()
            created += 1
        except IntegrityError:
            db.session.rollback()
