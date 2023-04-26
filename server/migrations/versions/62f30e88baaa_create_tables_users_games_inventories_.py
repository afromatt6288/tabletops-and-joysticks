"""Create tables users, games, inventories, swaps, messages, reviews, chat_rooms, chat_messages.

Revision ID: 62f30e88baaa
Revises: 
Create Date: 2023-04-26 09:21:10.790819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62f30e88baaa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('genre1', sa.String(), nullable=False),
    sa.Column('genre2', sa.String(), nullable=False),
    sa.Column('platform', sa.String(), nullable=False),
    sa.Column('player_num_min', sa.Integer(), nullable=False),
    sa.Column('player_num_max', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_games'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('_password_hash', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('avatar_url', sa.String(), nullable=True),
    sa.Column('stars', sa.Integer(), nullable=True),
    sa.Column('travel_distance', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('username', name=op.f('uq_users_username'))
    )
    op.create_table('chat_rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat_room_name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('chat_room_creator_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['chat_room_creator_user_id'], ['users.id'], name=op.f('fk_chat_rooms_chat_room_creator_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_chat_rooms'))
    )
    op.create_table('inventories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_inventories_game_id_games')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_inventories_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_inventories'))
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message_text', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('sender_user_id', sa.Integer(), nullable=True),
    sa.Column('receiver_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['receiver_user_id'], ['users.id'], name=op.f('fk_messages_receiver_user_id_users')),
    sa.ForeignKeyConstraint(['sender_user_id'], ['users.id'], name=op.f('fk_messages_sender_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_messages'))
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review_content', sa.String(), nullable=True),
    sa.Column('review_stars', sa.Integer(), nullable=True),
    sa.Column('review_date', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('review_sender_user_id', sa.Integer(), nullable=True),
    sa.Column('review_receiver_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['review_receiver_user_id'], ['users.id'], name=op.f('fk_reviews_review_receiver_user_id_users')),
    sa.ForeignKeyConstraint(['review_sender_user_id'], ['users.id'], name=op.f('fk_reviews_review_sender_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_reviews'))
    )
    op.create_table('swaps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('swap_status', sa.String(), nullable=False),
    sa.Column('borrow_date', sa.DateTime(), nullable=False),
    sa.Column('due_date', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('game_swapped_id', sa.Integer(), nullable=True),
    sa.Column('loaning_user_id', sa.Integer(), nullable=True),
    sa.Column('borrowing_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['borrowing_user_id'], ['users.id'], name=op.f('fk_swaps_borrowing_user_id_users')),
    sa.ForeignKeyConstraint(['game_swapped_id'], ['games.id'], name=op.f('fk_swaps_game_swapped_id_games')),
    sa.ForeignKeyConstraint(['loaning_user_id'], ['users.id'], name=op.f('fk_swaps_loaning_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_swaps'))
    )
    op.create_table('chat_messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat_message_text', sa.String(), nullable=True),
    sa.Column('chat_message_date', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('chat_sender_user_id', sa.Integer(), nullable=True),
    sa.Column('chat_room_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['chat_room_id'], ['chat_rooms.id'], name=op.f('fk_chat_messages_chat_room_id_chat_rooms')),
    sa.ForeignKeyConstraint(['chat_sender_user_id'], ['users.id'], name=op.f('fk_chat_messages_chat_sender_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_chat_messages'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chat_messages')
    op.drop_table('swaps')
    op.drop_table('reviews')
    op.drop_table('messages')
    op.drop_table('inventories')
    op.drop_table('chat_rooms')
    op.drop_table('users')
    op.drop_table('games')
    # ### end Alembic commands ###
