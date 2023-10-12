"""empty message

Revision ID: f6b0287fdcba
Revises: 
Create Date: 2023-10-11 14:40:10.202978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6b0287fdcba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('fields', sa.String(length=100000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('data',
    sa.Column('file_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(length=1000), nullable=True),
    sa.Column('line_number', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data')
    op.drop_table('file')
    # ### end Alembic commands ###
