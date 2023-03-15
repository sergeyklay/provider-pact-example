# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Schemes for handling (de)serialized model representation."""

from marshmallow import EXCLUDE, fields, post_dump, Schema, validate


class CategorySchema(Schema):
    """Schema for product categories."""

    class Meta:
        unknown = EXCLUDE

    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True,
        validate=validate.Length(
            min=1,
            max=64,
        ),
    )


class BrandSchema(Schema):
    """Schema for product brands."""

    class Meta:
        unknown = EXCLUDE

    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True,
        validate=validate.Length(
            min=1,
            max=64,
        ),
    )


class ProductQueryArgsSchema(Schema):
    bid = fields.Int()
    cid = fields.Int()
    q = fields.Str()


class ProductSchema(Schema):
    """Schema for products."""

    class Meta:
        unknown = EXCLUDE

    id = fields.Int(dump_only=True)

    name = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=64),
    )

    description = fields.Str(
        required=False,
        validate=validate.Length(max=512),
    )

    price = fields.Float(
        required=True,
        validate=validate.Range(0.0, min_inclusive=True),
    )

    discount = fields.Float(
        required=True,
        validate=validate.Range(0.0, min_inclusive=True),
    )

    rating = fields.Float(
        required=True,
        validate=validate.Range(
            0.0,
            5.0,
            min_inclusive=True,
            max_inclusive=True,
        ),
    )

    stock = fields.Int(
        required=True,
        validate=validate.Range(0, min_inclusive=True),
    )

    brand_id = fields.Int(required=True)
    category_id = fields.Int(required=True)

    created_at = fields.Function(
        lambda obj: obj.created_at.isoformat(timespec='milliseconds'),
        dump_only=True
    )

    updated_at = fields.Function(
        lambda obj: obj.updated_at.isoformat(timespec='milliseconds'),
        dump_only=True
    )

    @post_dump()
    def fix_datetimes(self, data, **_unused):
        data['created_at'] += 'Z'
        data['updated_at'] += 'Z'
        return data
