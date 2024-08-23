"""Add status column to jobs table

Revision ID: 4a76f79ec031
Revises: 6e477da0acf1
Create Date: 2024-08-22 16:43:51.112965

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a76f79ec031'
down_revision: Union[str, None] = '6e477da0acf1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('jobs', sa.Column('status', sa.String(), index=True))


def downgrade() -> None:
    op.drop_column('jobs', 'status')
