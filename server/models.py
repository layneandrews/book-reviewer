from ipdb import set_trace
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    _password_hash = db.Column(db.String)     

    serialize_rules = ("-_password_hash","-admin", "-created_at", "-updated_at")

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.String)
    genres = db.relationship('Genre', secondary='book_genres', back_populates='books')

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    text = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

class Genre(db.Model, SerializerMixin):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String)
    books = db.relationship('Book', secondary='book_genres', back_populates='genres')

class Book_genre(db.Model):
    __tablename__ = 'book_genres'
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True)
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)

