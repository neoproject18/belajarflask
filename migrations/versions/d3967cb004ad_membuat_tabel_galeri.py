"""Membuat tabel galeri

Revision ID: d3967cb004ad
Revises: 8cc3f5cdaf07
Create Date: 2021-12-13 10:44:28.841486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3967cb004ad'
down_revision = '8cc3f5cdaf07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('galeri',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('filename', sa.String(length=50), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('pathname', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('galeri')
    # ### end Alembic commands ###