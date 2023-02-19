# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(64), unique=True, index=True, nullable=False)
    description = db.Column(db.String(512), nullable=False, default='')
    price = db.Column(db.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=False, default=0.0)
    discount = db.Column(db.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=False, default=0.0)
    rating = db.Column(db.Numeric(precision=3, scale=2, decimal_return_scale=2), index=True, nullable=False, default=0.0)
    stock = db.Column(db.Integer, nullable=False, default=0)
    brand = db.Column(db.String(64), index=True, nullable=False)
    category = db.Column(db.String(64), index=True, nullable=False)

    def __repr__(self):
        """Returns the object representation in string format."""
        return '<Product %r>' % self.id
