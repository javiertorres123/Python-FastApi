"""create product file

Revision ID: f967bbfbc225
Revises: 
Create Date: 2025-12-01 19:32:25.733530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f967bbfbc225'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('description', sa.String(length=255), nullable=True),
        sa.Column('price_sale', sa.Float, nullable=False),
        sa.Column('price_buy', sa.Float, nullable=False),
        sa.Column('stock', sa.Integer, nullable=False),
        sa.Column('id_category', sa.Integer, sa.ForeignKey('categories.id'), nullable=False),
        sa.Column('status', sa.Boolean, nullable=False, default=True),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), onupdate=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table('products')
