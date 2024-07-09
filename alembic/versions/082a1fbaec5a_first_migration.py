"""First migration

Revision ID: 082a1fbaec5a
Revises: 1a150a60e19d
Create Date: 2024-07-09 14:48:10.662995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '082a1fbaec5a'
down_revision: Union[str, None] = '1a150a60e19d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
