from app import app
from models import db, User, Book, Review, Genre

users = []

u1 = User(name='Layne', username='landrews1127')
users.append(u1)
u2 = User(name='Garrett', username ='gbob99')
users.append(u2)

db.session.add_all(users)
db.session.commit()

#------------------------#

genres = []

g1 = Genre(genre_name='horror')
genres.append(g1)
g2 = Genre(genre_name='comedy')
genres.append(g2)

db.session.add_all(genres)
db.session.commit()

#------------------------#

books = []

b1 = Book(title='holes', author='Louis Sachar', description='A book about a boy, wrongfully convicted of theft who has to go to a desert boot camp and dig holes to pay for his crimes.', image_url='https://i0.wp.com/www.nationalbook.org/wp-content/uploads/2015/12/holes-louis-sachar-book-cover.jpg?fit=500%2C761&ssl=1')
books.append(b1)
db.session.add_all(books)
db.session.commit()




