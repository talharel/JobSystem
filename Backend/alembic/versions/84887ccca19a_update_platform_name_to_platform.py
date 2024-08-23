"""Update platform_name to platform

Revision ID: 84887ccca19a
Revises: 4a76f79ec031
Create Date: 2024-08-22 19:11:22.005470

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84887ccca19a'
down_revision: Union[str, None] = '4a76f79ec031'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('jobs', sa.Column('platform_name', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('jobs', 'platform_name')

