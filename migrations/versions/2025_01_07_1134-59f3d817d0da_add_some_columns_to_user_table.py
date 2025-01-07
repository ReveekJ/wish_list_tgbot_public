"""add some columns to user table

Revision ID: 59f3d817d0da
Revises: 517b5e6c41ed
Create Date: 2025-01-07 11:34:50.368711

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59f3d817d0da'
down_revision: Union[str, None] = '517b5e6c41ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the enum type first
    gender_enum = sa.Enum('MALE', 'FEMALE', 'UNSPECIFIED', name='genderenum')
    gender_enum.create(op.get_bind())  # Create the enum type in the database

    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('birthdate', sa.Date(), nullable=True))
    op.add_column('users', sa.Column('gender', sa.Enum('MALE', 'FEMALE', 'UNSPECIFIED', name='genderenum'), nullable=True))
    op.add_column('users', sa.Column('name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('username', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'username')
    op.drop_column('users', 'name')
    op.drop_column('users', 'gender')
    op.drop_column('users', 'birthdate')
    # ### end Alembic commands ###
    # Then drop the enum type
    gender_enum = sa.Enum('MALE', 'FEMALE', 'UNSPECIFIED', name='genderenum')
    gender_enum.drop(op.get_bind())  # Drop the enum type from the database

