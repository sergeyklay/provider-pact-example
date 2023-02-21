# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

import decimal

import sqlalchemy as sa
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm as so

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        """Save current model to the database."""
        db.session.add(self)
        db.session.commit()


class Product(BaseModel):
    __tablename__ = 'products'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)

    title: so.Mapped[str] = so.mapped_column(
        sa.String(64),
        unique=True,
        index=True,
        nullable=False,
    )

    description: so.Mapped[str] = so.mapped_column(
        sa.String(512),
        nullable=False,
        default='',
    )

    price: so.Mapped[decimal.Decimal] = so.mapped_column(
        sa.Numeric(precision=8, scale=2, decimal_return_scale=2),
        nullable=False,
        default=0.0,
    )

    discount: so.Mapped[decimal.Decimal] = so.mapped_column(
        sa.Numeric(precision=8, scale=2, decimal_return_scale=2),
        nullable=False,
        default=0.0,
    )

    rating: so.Mapped[decimal.Decimal] = so.mapped_column(
        sa.Numeric(precision=3, scale=2, decimal_return_scale=2),
        index=True,
        nullable=False,
        default=0.0,
    )

    stock: so.Mapped[int] = so.mapped_column(
        nullable=False,
        default=0,
    )

    brand: so.Mapped[str] = so.mapped_column(
        sa.String(64),
        index=True,
        nullable=False,
    )

    category: so.Mapped[str] = so.mapped_column(
        sa.String(64),
        index=True,
        nullable=False,
    )

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

    def __repr__(self):
        """Returns the object representation in string format."""
        return f'''<Product {self.id!r}>'''
