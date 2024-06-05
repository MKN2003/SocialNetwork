from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from database import Base


# Таблица пользовотеля
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    birthday = Column(String, nullable=False)
    user_city = Column(String, nullable=False)
    status = Column(String, nullable=False)
    reg_date = Column(DateTime)


# Хэштеги
class Hashtag(Base):
    __tablename__ = 'hashtags'
    id = Column(Integer, autoincrement=True, primary_key=True)
    hashtag_name = Column(String, nullable=False)
    reg_date = Column(DateTime)


# Посты пользовтеля
class UserPost(Base):
    __tablename__ = 'user_posts'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    main_text = Column(String, nullable=False)
    hashtag = Column(String, ForeignKey('hashtags.hashtag_name'), nullable=True)
    descriptions = Column(String, nullable=False)
    red_date = Column(DateTime)

    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')
    hashtag_fk = relationship(Hashtag, foreign_keys=[hashtag], lazy='subquery')


# Изображения
class PostPhoto(Base):
    __tablename__ = 'post_photo'
    id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey('user_posts.id'))
    photo_path = Column(String, nullable=False)
    reg_date = Column(DateTime)

    post_fk = relationship(UserPost, foreign_keys=[post_id], lazy='subquery')


# Комментрии
class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey('user_posts.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    comment_text = Column(String, nullable=False)
    reg_date = Column(DateTime)

    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')
    post_fk = relationship(UserPost, foreign_keys=[post_id], lazy='subquery')
