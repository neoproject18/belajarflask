"""merging two heads

Revision ID: b554d65808c3
Revises: 540019bae805, a2c7f4716abb
Create Date: 2021-12-12 14:58:02.618064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b554d65808c3'
down_revision = ('540019bae805', 'a2c7f4716abb')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
