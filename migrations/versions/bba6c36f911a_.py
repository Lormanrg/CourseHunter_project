"""empty message

Revision ID: bba6c36f911a
Revises: f9f6d1e9a255
Create Date: 2023-02-27 21:18:18.756674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bba6c36f911a'
down_revision = 'f9f6d1e9a255'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('img_url',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
        batch_op.alter_column('cloudinary_id',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('cloudinary_id',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
        batch_op.alter_column('img_url',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)

    # ### end Alembic commands ###
