import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# database engine object from SQLAlchemy that manages connections to the database
engine = create_engine(os.getenv("DATABASE_URL"))

# create a 'scoped session' that ensures different users' interactions with the
# database are kept separate
db = scoped_session(sessionmaker(bind=engine))

def main():
    books = db.execute("SELECT isbn, title, author, year FROM books WHERE year < '1946'").fetchall() 
    for book in books:
        print(f"{book.title} by {book.author} published in {book.year}.")

if __name__=="__main__":
    main()