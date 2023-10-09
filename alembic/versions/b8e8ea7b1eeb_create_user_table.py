"""create user table

Revision ID: b8e8ea7b1eeb
Revises: 
Create Date: 2023-10-09 14:23:11.454121

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8e8ea7b1eeb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), unique=False),
        sa.Column('email', sa.String(120), unique=True),
    )


def downgrade() -> None:
    op.drop_table('user')
