import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Table
from sqlalchemy.orm import relationship, declarative_base, backref
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


followers = Table('followers', Base.metadata ,
    Column('follower_id', Integer, ForeignKey('follower.id'),  primary_key=True),
    Column('following_id',Integer, ForeignKey('user.id'),  primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    followers = relationship('Follower', secondary=followers , lazy='subquery', backref= backref('user', lazy=True))
    # following = relationship('User', secondary='follower', back_populates='followers', lazy=True)
    posts = relationship('Post', backref='user', lazy=True)
    user_comments = relationship('Comment', backref='user', lazy=True)

    def to_dict(self):
        return {}

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)

    def to_dict(self):
        return {}
        
class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    
    def to_dict(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_comments = relationship('Comment', backref='post', lazy=True)
    medias = relationship('Media', backref='post', lazy=True)
    
    def to_dict(self):
        return {}

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(Enum)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
