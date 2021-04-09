#import packages
from flask import Flask, render_template, redirect, request
from flaskext.mysql import MySQL

#create application instance
app = Flask(__name__)

#connect to db
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Harrypot78!.'
app.config['MYSQL_DATABASE_DB'] = 'book_business'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def index():
    return redirect('/viewBooks')



#@app.route('/update', methods=['POST'])
#def add():
#    book = request.form
#    id = book['id']
#    name = book['title']
#    cur = mysql.get_db().cursor()
#    cur.execute("UPDATE books SET BookTitle=%s WHERE BookID=%s",(name, id))
#    mysql.get_db().commit()
#    return redirect('/read')

#@app.route('/read')
#def read():
#    cursor = mysql.get_db().cursor()
#    response = cursor.execute("SELECT * FROM books")
#    html = ''    
#    if response > 0:
#        books = cursor.fetchall()
#        return render_template('read.html', list=books)



#########################################
## BOOKS
#########################################
#create read and update screen for books

#screen for viewing books in DB 
@app.route('/viewBooks', methods=['GET','POST'])
def viewBooks():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM books")
    html = ''    
    if response > 0:
        books = cursor.fetchall()
        return render_template('viewBooks.html', list=books)

#screen for creating books in DB
@app.route('/createBooks')
def createBooks():
    return render_template('/createBooks.html')

#screen for modifying books in DB (add options for 'edit' and 'delete')
@app.route('/modifyBooks', methods=['GET','POST'])
def modifyBooks():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM books")
    html = ''    
    if response > 0:
        books = cursor.fetchall()
        return render_template('readBooks.html', list=books)


#screen for editing single book in DB
@app.route('/book')
def book():
    book = {}
    book['id'] = request.args.get('id')
    book['name'] = request.args.get('name')
    book['genre'] = request.args.get('genre')
    book['publisher'] = request.args.get('publisher')
    book['year'] = request.args.get('year')
    book['price'] = request.args.get('price')
    
    return render_template('editBooks.html', book=book)

#method for creating new books in DB
@app.route('/createNewBook', methods=['POST'])
def addNewBook():
    # Fetch form data
    book = request.form
    title = book['title']
    genre = book['genre']
    PubID = book['publisher']
    PubYear = book['year']
    price = book['price']
    cur = mysql.get_db().cursor()
    cur.execute("INSERT INTO books(BookTitle, Genre, PublisherID, PublicationYear, Price) VALUES(%s, %s, %s, %s, %s)",(title, genre, PubID, PubYear, price))
    mysql.get_db().commit()
    return redirect('/viewBooks')

#method for modifying books in DB
@app.route('/updateBooks', methods=['POST'])
def addBook():
    book = request.form
    id = book['id']
    name = book['title']
    genre = book['genre']
    publisher = book['publisher']
    year = book['year']
    price = book['price']

    cur = mysql.get_db().cursor()
    cur.execute("UPDATE books SET BookTitle=%s WHERE BookID=%s",(name, id))
    cur.execute("UPDATE books SET Genre=%s WHERE BookID=%s",(genre, id))
    cur.execute("UPDATE books SET PublisherID=%s WHERE BookID=%s",(publisher, id))
    cur.execute("UPDATE books SET PublicationYear=%s WHERE BookID=%s",(year, id))
    cur.execute("UPDATE books SET Price=%s WHERE BookID=%s",(price, id))

    mysql.get_db().commit()
    return redirect('/modifyBooks')

#method for deleting a book in DB
@app.route('/delete')
def delete():
    id = request.args.get('id')
    cur = mysql.get_db().cursor()
    cur.execute("DELETE FROM books WHERE BookID=%s",id)
    mysql.get_db().commit()
    return redirect('/modifyBooks')


#########################################
## Publishers
#########################################
#create read and update screen for books

#screen for viewing publishers in DB 
@app.route('/viewPublishers', methods=['GET','POST'])
def viewPublishers():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM publishers")
    html = ''    
    if response > 0:
        publishers = cursor.fetchall()
        return render_template('viewPublishers.html', list=publishers)

#screen for creating publishers in DB
@app.route('/createPublishers')
def createPublishers():
    return render_template('/createPublishers.html')

#screen for modifying publishers in DB (add options for 'edit' and 'delete')
@app.route('/modifyPublishers', methods=['GET','POST'])
def modifyPublishers():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM publishers")
    html = ''    
    if response > 0:
        publishers = cursor.fetchall()
        return render_template('readPublishers.html', list=publishers)


#screen for editing single publisher in DB
@app.route('/publisher')
def publisher():
    publisher = {}
    publisher['id'] = request.args.get('id')
    publisher['name'] = request.args.get('name')
    publisher['city'] = request.args.get('city')
    publisher['region'] = request.args.get('region')
    publisher['country'] = request.args.get('country')
    
    return render_template('editPublishers.html', publisher=publisher)

#method for creating new publishers in DB
@app.route('/createNewPublisher', methods=['POST'])
def addNewPublisher():
    # Fetch form data
    publisher = request.form
    name = publisher['name']
    city = publisher['city']
    region = publisher['region']
    country = publisher['country']

    cur = mysql.get_db().cursor()
    cur.execute("INSERT INTO publishers(PublisherName, City, Region, Country) VALUES(%s, %s, %s, %s)",(name, city, region, country))
    mysql.get_db().commit()
    return redirect('/viewPublishers')

#method for modifying publishers in DB
@app.route('/updatePublishers', methods=['POST'])
def addPublisher():
    publisher = request.form
    id = publisher['id']
    name = publisher['name']
    city = publisher['city']
    region = publisher['region']
    country = publisher['country']

    cur = mysql.get_db().cursor()
    cur.execute("UPDATE publishers SET PublisherName=%s WHERE PublisherID=%s",(name, id))
    cur.execute("UPDATE publishers SET City=%s WHERE PublisherID=%s",(city, id))
    cur.execute("UPDATE publishers SET Region=%s WHERE PublisherID=%s",(region, id))
    cur.execute("UPDATE publishers SET Country=%s WHERE PublisherID=%s",(country, id))

    mysql.get_db().commit()
    return redirect('/modifyPublishers')

#method for deleting a publisher from DB
@app.route('/deletePublishers')
def deletePublishers():
    id = request.args.get('id')
    cur = mysql.get_db().cursor()
    cur.execute("DELETE FROM publishers WHERE PublisherID=%s",id)
    mysql.get_db().commit()
    return redirect('/modifyPublishers')




#########################################
## AUTHORS
#########################################

#create read and update screen for authors

#screen for viewing authors in DB
@app.route('/viewAuthors', methods=['GET','POST'])
def viewAuthors():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM authors")
    html = ''    
    if response > 0:
        authors = cursor.fetchall()
        return render_template('viewAuthors.html', list=authors)

#screen for creating authors in DB
@app.route('/createAuthors')
def createAuthors():
    return render_template('/createAuthors.html')

#screen for modifying authors in DB (add options for 'edit' and 'delete')
@app.route('/modifyAuthors', methods=['GET','POST'])
def modifyAuthors():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM authors")
    html = ''    
    if response > 0:
        authors = cursor.fetchall()
        return render_template('readAuthors.html', list=authors)

#screen for editing single author in DB
@app.route('/author')
def author():
    author = {}
    author['id'] = request.args.get('id')
    author['firstname'] = request.args.get('firstname')
    author['lastname'] = request.args.get('lastname')    
    author['origin'] = request.args.get('origin')        
    return render_template('editAuthors.html', author=author)

#method for creating new authors in DB
@app.route('/create', methods=['POST'])
def addNewAuthor():
    # Fetch form data
    author = request.form
    firstname = author['firstname']
    lastname = author['lastname']
    origin = author['origin']
    cur = mysql.get_db().cursor()
    cur.execute("INSERT INTO authors(FirstName, LastName, Country) VALUES(%s, %s, %s)",(firstname, lastname, origin))
    mysql.get_db().commit()
    return redirect('/viewAuthors')

#method for modifying authors in DB
@app.route('/updateAuthors', methods=['POST'])
def addAuthor():
    author = request.form
    id = author['id']
    firstname = author['firstname']
    lastname = author['lastname']
    origin = author['origin']
    cur = mysql.get_db().cursor()
    cur.execute("UPDATE authors SET FirstName=%s WHERE AuthorID=%s",(firstname, id))
    cur.execute("UPDATE authors SET LastName=%s WHERE AuthorID=%s",(lastname, id))
    cur.execute("UPDATE authors SET Country=%s WHERE AuthorID=%s",(origin, id))
    mysql.get_db().commit()
    return redirect('/modifyAuthors')

#method for deleting authors from DB
@app.route('/deleteAuthors')
def deleteAuthors():
    id = request.args.get('id')
    cur = mysql.get_db().cursor()
    cur.execute("DELETE FROM authors WHERE AuthorID=%s",id)
    mysql.get_db().commit()
    return redirect('/modifyAuthors')


# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)