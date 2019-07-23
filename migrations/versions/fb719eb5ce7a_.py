"""empty message

Revision ID: fb719eb5ce7a
Revises: 
Create Date: 2019-07-22 18:16:06.907662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb719eb5ce7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('domains_csv',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('domain', sa.String(length=256), nullable=True),
    sa.Column('first_seen', sa.Integer(), nullable=True),
    sa.Column('last_seen', sa.Integer(), nullable=True),
    sa.Column('etld', sa.String(length=256), nullable=True),
    sa.Column('time_date_imported', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('search',
    sa.Column('id', sa.String(length=256), nullable=False),
    sa.Column('keyword', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('results',
    sa.Column('domain_id', sa.Integer(), nullable=False),
    sa.Column('search_id', sa.String(length=256), nullable=False),
    sa.ForeignKeyConstraint(['domain_id'], ['domains_csv.id'], ),
    sa.ForeignKeyConstraint(['search_id'], ['search.id'], ),
    sa.PrimaryKeyConstraint('domain_id', 'search_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    op.drop_table('search')
    op.drop_table('domains_csv')
    # ### end Alembic commands ###