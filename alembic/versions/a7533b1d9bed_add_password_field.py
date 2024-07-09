"""add  password field

Revision ID: a7533b1d9bed
Revises: 082a1fbaec5a
Create Date: 2024-07-09 14:51:55.347265

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7533b1d9bed'
down_revision: Union[str, None] = '082a1fbaec5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
