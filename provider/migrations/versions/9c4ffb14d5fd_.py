# This file is part of the Contract Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""

Revision ID: 9c4ffb14d5fd
Revises:
Create Date: 2023-02-19 12:49:26.068212

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '9c4ffb14d5fd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    price_column = sa.Numeric(precision=8, scale=2, decimal_return_scale=2)
    rating_column = sa.Numeric(precision=3, scale=2, decimal_return_scale=2)

    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=64), nullable=False),
        sa.Column('description', sa.String(length=512), nullable=False),
        sa.Column('price', price_column, nullable=False),
        sa.Column('discount', price_column, nullable=False),
        sa.Column('rating', rating_column, nullable=False),
        sa.Column('stock', sa.Integer(), nullable=False),
        sa.Column('brand', sa.String(length=64), nullable=False),
        sa.Column('category', sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint('id'))

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f('ix_products_brand'), ['brand'], unique=False)
        batch_op.create_index(
            batch_op.f('ix_products_category'), ['category'], unique=False)
        batch_op.create_index(
            batch_op.f('ix_products_rating'), ['rating'], unique=False)
        batch_op.create_index(
            batch_op.f('ix_products_title'), ['title'], unique=True)


def downgrade():
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_products_title'))
        batch_op.drop_index(batch_op.f('ix_products_rating'))
        batch_op.drop_index(batch_op.f('ix_products_category'))
        batch_op.drop_index(batch_op.f('ix_products_brand'))

    op.drop_table('products')
