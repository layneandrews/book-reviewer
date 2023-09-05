from ipdb import set_trace
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

db = SQLAlchemy()

book_genres = db.Table('book_genres',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    text = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    reviews = db.relationship('Review', backref='user', lazy=True)
    books = db.relationship('Book', backref='users', secondary=Review.__table__)
    #auth    

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    description = db.Column(db.Text)
    image_url = db.Column(db.String)
    genres = db.relationship('Genre', secondary=book_genres, back_populates='books')
    reviews = db.relationship('Review', backref='Book', lazy=True)

class Genre(db.Model, SerializerMixin):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String)
    books = db.relationship('Book', secondary=book_genres, back_populates='genres')


