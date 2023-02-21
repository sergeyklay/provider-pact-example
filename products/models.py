# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

from flask import url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'products'

    price_column = db.Numeric(precision=8, scale=2, decimal_return_scale=2)
    rating_column = db.Numeric(precision=3, scale=2, decimal_return_scale=2)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, index=True, nullable=False)
    description = db.Column(db.String(512), nullable=False, default='')
    price = db.Column(price_column, nullable=False, default=0.0)
    discount = db.Column(price_column, nullable=False, default=0.0)
    rating = db.Column(rating_column, index=True, nullable=False, default=0.0)
    stock = db.Column(db.Integer, nullable=False, default=0)
    brand = db.Column(db.String(64), index=True, nullable=False)
    category = db.Column(db.String(64), index=True, nullable=False)

    def get_url(self):
        return url_for('api.get_product', product_id=self.id, _external=True)

    def export_data(self):
        return {
            'self_url': self.get_url(),
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': float(self.price),
            'discount': float(self.discount),
            'rating': float(self.rating),
            'stock': int(self.stock),
            'brand': self.brand,
            'category': self.category,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        """Returns the object representation in string format."""
        return f'''<Product {self.id!r}>'''
