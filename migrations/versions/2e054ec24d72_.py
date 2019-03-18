"""empty message

Revision ID: 2e054ec24d72
Revises: 9cac3a13c3c8
Create Date: 2019-03-17 22:02:36.815415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e054ec24d72'
down_revision = '9cac3a13c3c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('biography', sa.String(length=1000), nullable=True))
    op.add_column('user_profiles', sa.Column('email', sa.String(length=80), nullable=True))
    op.add_column('user_profiles', sa.Column('fname', sa.String(length=40), nullable=True))
    op.add_column('user_profiles', sa.Column('gender', sa.String(length=6), nullable=True))
    op.add_column('user_profiles', sa.Column('image', sa.String(length=40), nullable=True))
    op.add_column('user_profiles', sa.Column('lname', sa.String(length=40), nullable=True))
    op.add_column('user_profiles', sa.Column('location', sa.String(length=80), nullable=True))
    op.add_column('user_profiles', sa.Column('logtime', sa.String(length=40), nullable=True))
    op.drop_constraint('user_profiles_username_key', 'user_profiles', type_='unique')
    op.create_unique_constraint(None, 'user_profiles', ['email'])
    op.drop_column('user_profiles', 'username')
    op.drop_column('user_profiles', 'first_name')
    op.drop_column('user_profiles', 'last_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('last_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.add_column('user_profiles', sa.Column('first_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.add_column('user_profiles', sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user_profiles', type_='unique')
    op.create_unique_constraint('user_profiles_username_key', 'user_profiles', ['username'])
    op.drop_column('user_profiles', 'logtime')
    op.drop_column('user_profiles', 'location')
    op.drop_column('user_profiles', 'lname')
    op.drop_column('user_profiles', 'image')
    op.drop_column('user_profiles', 'gender')
    op.drop_column('user_profiles', 'fname')
    op.drop_column('user_profiles', 'email')
    op.drop_column('user_profiles', 'biography')
    # ### end Alembic commands ###