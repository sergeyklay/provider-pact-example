# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

from faker import Faker
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, index=True, nullable=False)
    description = db.Column(db.String(512), nullable=False, default='')
    price = db.Column(db.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=False, default=0.0)
    discount = db.Column(db.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=False, default=0.0)
    rating = db.Column(db.Numeric(precision=3, scale=2, decimal_return_scale=2), index=True, nullable=False, default=0.0)
    stock = db.Column(db.Integer, nullable=False, default=0)
    brand = db.Column(db.String(64), index=True, nullable=False)
    category = db.Column(db.String(64), index=True, nullable=False)

    @classmethod
    def seed(cls, fake: Faker):
        from faker.providers import company, lorem, python
        from provider.fake import FakeProduct

        fake.add_provider(company)
        fake.add_provider(lorem)
        fake.add_provider(python)
        fake.add_provider(FakeProduct)

        price = fake.pyfloat(left_digits=3, right_digits=2, min_value=1.0, max_value=999.99)
        product = Product(
            title=' '.join(fake.words(nb=5)).capitalize(),
            description=fake.sentence(nb_words=10),
            price=price,
            discount=fake.pyfloat(left_digits=3, right_digits=2, min_value=0.0, max_value=price),
            rating=fake.pyfloat(left_digits=1, right_digits=2, min_value=0.0, max_value=5.0),
            stock=fake.pyint(min_value=0, max_value=999),
            brand=fake.company(),
            category=fake.category(),
        )
        product.save()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        """Returns the object representation in string format."""
        return '<Product %r>' % self.id
