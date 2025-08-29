from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)

with app.app_context():
    db.create_all()


all_books = []


@app.route('/')
def home():
    books = db.session.execute(db.select(Books).order_by(Books.id)).scalars()
    return render_template("index.html",all_books = books)


@app.route("/add",methods=['POST','GET'])
def add():
    if request.method == 'POST':
        book = Books(title = request.form['book_name'],author  = request.form['book_author'],rating = request.form['rating'])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home')) 
    return render_template("add.html")

@app.route("/edit/<id>",methods=['POST','GET'])
def edit(id):
    books_by_id = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
    return render_template('edit.html',all_books = books_by_id)

if __name__ == "__main__":
    app.run(debug=True)

