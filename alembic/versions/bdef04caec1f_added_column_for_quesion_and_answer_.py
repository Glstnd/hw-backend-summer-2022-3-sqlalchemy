"""Added column for quesion and answer models 2.0

Revision ID: bdef04caec1f
Revises: 005f5d103e4e
Create Date: 2024-04-23 03:02:14.055993

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bdef04caec1f'
down_revision: Union[str, None] = '005f5d103e4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###