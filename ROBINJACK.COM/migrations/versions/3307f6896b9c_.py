"""empty message

Revision ID: 3307f6896b9c
Revises: dd3382e1c388
Create Date: 2019-10-12 17:03:58.801580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3307f6896b9c'
down_revision = 'dd3382e1c388'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_message_timestamp'), 'message', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_message_timestamp'), table_name='message')
    op.drop_column('message', 'timestamp')
    # ### end Alembic commands ###
