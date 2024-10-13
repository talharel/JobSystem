"""Job Table

Revision ID: d2a783c23768
Revises: 
Create Date: 2024-08-14 12:37:45.268063

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'd2a783c23768'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'jobs',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('company_name', sa.String(), nullable=True),
        sa.Column('url', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('url'),
        sa.Index('ix_jobs_company_name', 'company_name'),
    )


def downgrade() -> None:
    op.drop_table('jobs')
