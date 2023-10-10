"""Added API tokens

Revision ID: c99453498b92
Revises: b346dcd75c14
Create Date: 2023-02-16 00:16:35.538828

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = 'c99453498b92'
down_revision = 'b346dcd75c14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('key', sqlalchemy_utils.types.encrypted.encrypted_type.EncryptedType(), nullable=False),
    sa.Column('organization', sa.String(length=80), nullable=False),
    sa.Column('revoked', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('api_token')
    # ### end Alembic commands ###