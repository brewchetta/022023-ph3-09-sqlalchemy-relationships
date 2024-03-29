"""empty message

Revision ID: d8b95c3fd833
Revises: be13140dfec8
Create Date: 2023-04-20 11:28:51.054638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8b95c3fd833'
down_revision = 'be13140dfec8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('movie_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_roles_movie_id_movies'), 'roles', 'movies', ['movie_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_roles_movie_id_movies'), 'roles', type_='foreignkey')
    op.drop_column('roles', 'movie_id')
    # ### end Alembic commands ###
