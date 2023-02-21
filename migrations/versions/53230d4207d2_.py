# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""empty message

Revision ID: 53230d4207d2
Revises: 9c4ffb14d5fd
Create Date: 2023-02-21 16:32:27.226662

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '53230d4207d2'
down_revision = '9c4ffb14d5fd'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_categories')))

    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f('ix_categories_name'),
            ['name'],
            unique=True,
        )

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('category_id', sa.Integer(), nullable=False)
        )
        batch_op.drop_index('ix_products_category')
        batch_op.create_foreign_key(
            batch_op.f('fk_products_category_id_categories'),
            'categories',
            ['category_id'],
            ['id'],
        )
        batch_op.drop_column('category')


def downgrade():
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('category', sa.VARCHAR(length=64), nullable=False)
        )
        batch_op.drop_constraint(
            batch_op.f('fk_products_category_id_categories'),
            type_='foreignkey',
        )
        batch_op.create_index(
            'ix_products_category',
            ['category'],
            unique=False,
        )
        batch_op.drop_column('category_id')

    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_categories_name'))

    op.drop_table('categories')
