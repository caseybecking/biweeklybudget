"""adding pools

Revision ID: 71d5421c7007
Revises: 6d37400ea9cd
Create Date: 2017-11-26 18:56:45.294188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71d5421c7007'
down_revision = '6d37400ea9cd'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'pool',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('gallons', sa.Numeric(precision=4, scale=4)),
        sa.Column('pool_type',sa.String(length=70)),
        mysql_engine='InnoDB'
    )


def downgrade():
    op.drop_table('pool')
