# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Add AuditMixin and IdentityMixin

Revision ID: 95ede4d5672e
Revises: 3602afd0b965
Create Date: 2023-03-11 11:19:16.415412

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '95ede4d5672e'
down_revision = '3602afd0b965'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('brands', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'created_at',
                sa.DateTime(timezone=True),
                server_default=sa.text('(CURRENT_TIMESTAMP)'),
                nullable=False,
            )
        )

        batch_op.add_column(
            sa.Column(
                'updated_at',
                sa.DateTime(timezone=True),
                server_default=sa.text('(CURRENT_TIMESTAMP)'),
                nullable=False,
            )
        )

        batch_op.create_index(
            batch_op.f('ix_brands_created_at'),
            ['created_at'],
            unique=False,
        )

        batch_op.create_index(
            batch_op.f('ix_brands_updated_at'),
            ['updated_at'],
            unique=False,
        )

    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'created_at',
                sa.DateTime(timezone=True),
                server_default=sa.text('(CURRENT_TIMESTAMP)'),
                nullable=False,
            )
        )

        batch_op.add_column(
            sa.Column(
                'updated_at',
                sa.DateTime(timezone=True),
                server_default=sa.text('(CURRENT_TIMESTAMP)'),
                nullable=False,
            )
        )

        batch_op.create_index(
            batch_op.f('ix_categories_created_at'),
            ['created_at'],
            unique=False,
        )

        batch_op.create_index(
            batch_op.f('ix_categories_updated_at'),
            ['updated_at'],
            unique=False,
        )

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('name', sa.String(length=64), nullable=False)
        )
        batch_op.add_column(
            sa.Column(
                'created_at',
                sa.DateTime(timezone=True),
                server_default=sa.text('(CURRENT_TIMESTAMP)'),
                nullable=False,
            )
        )

        batch_op.add_column(
            sa.Column(
                'updated_at',
                sa.DateTime(timezone=True),
                server_default=sa.text('(CURRENT_TIMESTAMP)'),
                nullable=False,
            )
        )

        batch_op.drop_index('ix_products_title')

        batch_op.create_index(
            batch_op.f('ix_products_created_at'),
            ['created_at'],
            unique=False,
        )

        batch_op.create_index(
            batch_op.f('ix_products_name'),
            ['name'],
            unique=True,
        )

        batch_op.create_index(
            batch_op.f('ix_products_updated_at'),
            ['updated_at'],
            unique=False,
        )

        batch_op.drop_column('title')


def downgrade():
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('title', sa.VARCHAR(length=64), nullable=False))
        batch_op.drop_index(batch_op.f('ix_products_updated_at'))
        batch_op.drop_index(batch_op.f('ix_products_name'))
        batch_op.drop_index(batch_op.f('ix_products_created_at'))
        batch_op.create_index('ix_products_title', ['title'], unique=False)
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('name')

    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_categories_updated_at'))
        batch_op.drop_index(batch_op.f('ix_categories_created_at'))
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    with op.batch_alter_table('brands', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_brands_updated_at'))
        batch_op.drop_index(batch_op.f('ix_brands_created_at'))
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
