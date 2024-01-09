"""removed errors

Revision ID: dfdf6e8fd3c1
Revises: cb16cca66947
Create Date: 2023-12-22 18:19:30.151815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfdf6e8fd3c1'
down_revision = 'cb16cca66947'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'restaurants', ['restaurant_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'pizzas', ['pizza_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'restaurants', ['restaurant_id'], ['id'])
        batch_op.create_foreign_key(None, 'pizzas', ['pizza_id'], ['id'])

    # ### end Alembic commands ###
