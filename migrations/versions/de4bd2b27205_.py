"""empty message

Revision ID: de4bd2b27205
Revises: 
Create Date: 2023-02-19 12:37:55.412027

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'de4bd2b27205'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('title', sa.String(length=64), nullable=False),
        sa.Column('description', sa.String(length=512), nullable=False),
        sa.Column('price', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=False),
        sa.Column('discount', sa.Numeric(precision=8, scale=2, decimal_return_scale=2), nullable=False),
        sa.Column('rating', sa.Numeric(precision=3, scale=2, decimal_return_scale=2), nullable=False),
        sa.Column('stock', sa.Integer(), nullable=False),
        sa.Column('brand', sa.String(length=64), nullable=False),
        sa.Column('category', sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint('id'))

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_products_brand'), ['brand'], unique=False)
        batch_op.create_index(batch_op.f('ix_products_category'), ['category'], unique=False)
        batch_op.create_index(batch_op.f('ix_products_rating'), ['rating'], unique=False)
        batch_op.create_index(batch_op.f('ix_products_title'), ['title'], unique=True)


def downgrade():
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_products_title'))
        batch_op.drop_index(batch_op.f('ix_products_rating'))
        batch_op.drop_index(batch_op.f('ix_products_category'))
        batch_op.drop_index(batch_op.f('ix_products_brand'))

    op.drop_table('products')
