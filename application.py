import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
        books = db.execute("SELECT * FROM books WHERE year > '1965'").fetchall()
        return render_template("index.html", books=books)

@app.route('/select', methods=["POST"])
def select():
    """Select a book"""

    name = request.form.get("name")
    try:
        year = int(requst.form.get("book-list"))
    except ValueError:
        return render_template("error.html", message="Invalid Something.")

# Make sure the year exists.
    if db.execute("SELECT * FROM books WHERE year = :year", {"year": year}).rowcount == 0:
        return render_template("error.html", message="No such flight with that id.")
    # db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
    #         {"name": name, "flight_id": flight_id})
    db.commit()
    return render_template("success.html")