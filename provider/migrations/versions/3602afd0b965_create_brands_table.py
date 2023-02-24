# This file is part of the Contract Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Create brands table

Revision ID: 3602afd0b965
Revises: 53230d4207d2
Create Date: 2023-02-21 17:51:22.686453

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '3602afd0b965'
down_revision = '53230d4207d2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'brands',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_brands')))

    with op.batch_alter_table('brands', schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f('ix_brands_name'),
            ['name'],
            unique=True,
        )

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('brand_id', sa.Integer(), nullable=False))
        batch_op.drop_index('ix_products_brand')
        batch_op.create_foreign_key(
            batch_op.f('fk_products_brand_id_brands'),
            'brands',
            ['brand_id'],
            ['id'],
        )
        batch_op.drop_column('brand')


def downgrade():
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('brand', sa.VARCHAR(length=64), nullable=False))
        batch_op.drop_constraint(
            batch_op.f('fk_products_brand_id_brands'),
            type_='foreignkey',
        )
        batch_op.create_index('ix_products_brand', ['brand'], unique=False)
        batch_op.drop_column('brand_id')

    with op.batch_alter_table('brands', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_brands_name'))

    op.drop_table('brands')
