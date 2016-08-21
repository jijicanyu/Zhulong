"""add is_active

Revision ID: 39b61b9700c2
Revises: None
Create Date: 2016-08-21 14:10:30.675618

"""

# revision identifiers, used by Alembic.
revision = '39b61b9700c2'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('zhulong_user', sa.Column('is_active', sa.BOOLEAN(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('zhulong_user', 'is_active')
    ### end Alembic commands ###