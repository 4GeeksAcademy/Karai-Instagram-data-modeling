import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Random_user_1(Base):
    __tablename__ = 'user_1'
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    first_name = Column(String(250))
    email = Column(String(250))

class Random_user_2(Base):
    __tablename__ = 'user_2'
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    first_name = Column(String(250))
    email = Column(String(250))


class likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    post_id = Column(String(250), ForeignKey('post.id'))
    liker_user = Column(Integer, ForeignKey('user_1.id'))
    liked_user = Column(Integer, ForeignKey('user_2.id'))

class comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    post_id = Column(String(250), ForeignKey('post.id'))
    commenter_user = Column(Integer, ForeignKey('user_1.id'))
    commented_user = Column(Integer, ForeignKey('user_2.id'))


class post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250), ForeignKey('user_2.id'))
    url = Column(String(250))




# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
