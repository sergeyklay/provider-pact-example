# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

import decimal
from typing import List

import sqlalchemy as sa
from flask import url_for
from sqlalchemy import orm as so

from .app import db
from .exceptions import ValidationError


class Product(db.Model):
    __tablename__ = 'products'

    id: so.Mapped[int] = so.mapped_column(
        primary_key=True,
        autoincrement=True,
    )

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

    brand_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey('brands.id'),
        nullable=False
    )

    brand: so.Mapped['Brand'] = so.relationship(
        back_populates='product',
    )

    category_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey('categories.id'),
        nullable=False
    )

    category: so.Mapped['Category'] = so.relationship(
        back_populates='product',
    )

    def get_url(self):
        return url_for('api.get_product', product_id=self.id, _external=True)

    def export_data(self):
        """Export data from a Flask application's database."""
        return {
            'self_url': self.get_url(),
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': float(self.price),
            'discount': float(self.discount),
            'rating': float(self.rating),
            'stock': self.stock,
            'brand': self.brand.name,
            'category': self.category.name,
        }

    def import_data(self, data):
        """Import data into a Flask application's database."""
        try:
            self.title = data['title']
            self.description = data['description']
            self.price = data['price']
            self.discount = data['discount']
            self.rating = data['rating']
            self.stock = data['stock']
            self.brand_id = data['brand_id']
            self.category_id = data['category_id']
        except KeyError as exc:
            raise ValidationError(
                f'Invalid product: missing {exc.args[0]}') from exc
        return self

    def __repr__(self):
        """Returns the object representation in string format."""
        return f'''<Product {self.id!r}>'''


class Category(db.Model):
    __tablename__ = 'categories'

    id: so.Mapped[int] = so.mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    name: so.Mapped[str] = so.mapped_column(
        sa.String(64),
        unique=True,
        index=True,
        nullable=False,
    )

    product: so.Mapped[List['Product']] = so.relationship(
        back_populates='category',
    )

    def __repr__(self):
        """Returns the object representation in string format."""
        return f'''<Category {self.id!r}>'''


class Brand(db.Model):
    __tablename__ = 'brands'

    id: so.Mapped[int] = so.mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    name: so.Mapped[str] = so.mapped_column(
        sa.String(64),
        unique=True,
        index=True,
        nullable=False,
    )

    product: so.Mapped[List['Product']] = so.relationship(
        back_populates='brand',
    )

    def __repr__(self):
        """Returns the object representation in string format."""
        return f'''<Brand {self.id!r}>'''
