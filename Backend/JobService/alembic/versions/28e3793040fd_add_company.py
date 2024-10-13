"""add Company

Revision ID: 28e3793040fd
Revises: 84887ccca19a
Create Date: 2024-08-27 15:29:44.219979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28e3793040fd'
down_revision: Union[str, None] = '84887ccca19a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'companies',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('company_name', sa.String(), index=True),
        sa.Column('url', sa.String())
    )


def downgrade() -> None:
    op.drop_table('companies')

