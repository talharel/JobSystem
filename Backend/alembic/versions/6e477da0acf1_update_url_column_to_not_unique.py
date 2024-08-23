"""Update url column to not unique

Revision ID: 6e477da0acf1
Revises: d2a783c23768
Create Date: 2024-08-14 15:01:40.050646

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '6e477da0acf1'
down_revision: Union[str, None] = 'd2a783c23768'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint('jobs_url_key', 'jobs', type_='unique')
    op.alter_column('jobs', 'url',
                    existing_type=sa.VARCHAR(),
                    nullable=True)



def downgrade() -> None:
    op.create_unique_constraint('jobs_url_key', 'jobs', ['url'])
