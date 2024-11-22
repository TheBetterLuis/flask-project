from app import mysql

#GET
def get_all():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT b.id as 'Book ID',b.title as 'Book Name',a.name as 'Author Name',g.name as 'Genre',r.content as 'Review Text',u.name as 'Review User'FROM books b join authors a on b.author_id = a.id join genres g on b.genre_id = g.id join reviews r on b.id = r.book_id join users u on r.user_id = u.id")
        columns = [column[0] for column in cursor.description]
        books = [dict(zip(columns,row)) for row in cursor.fetchall()]
        cursor.close()
        return books
    except Exception as e:
        print(f"Error fetching data: {str(e)}")
        return {"error":"Failed to fetching data"}

def get_books():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM books')
        columns = [column[0] for column in cursor.description]
        books = [dict(zip(columns,row)) for row in cursor.fetchall()]
        cursor.close()
        return books
    except Exception as e:
        print(f"Error fetching books: {str(e)}")
        return {"error":"Failed to fetch books"}

def get_book(id):
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM books WHERE id = %s',(id,))
        columns = [column[0] for column in cursor.description]
        response = dict(zip(columns,cursor.fetchone()))
        print(response)
        cursor.close()

        if response:
            return response
        else:
            return {"message":"Can't find book"}
    except Exception as e:
        print(f"Error fetching book: {str(e)}")
        return {"message":"Error fetching book"}       

def get_book_query(id):
    if id:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM books WHERE id = %s',(id,))
        response=cursor.fetchone()
        cursor.close()

        if response:
            return response
        else:
            return {"message":"Can't find user"}
    else:
        return {"message":"Must send ID"}

#POST
def create_book(data):
    title = data.get('title')
    published_date = data.get('published_date')
    author_id = data.get('author_id')
    genre_id = data.get('genre_id')
    editorial_id= data.get('editorial_id')

    if not title or not published_date or not author_id or not genre_id or not editorial_id:
        return {"message":"All fields are mandatory"}
    try: 
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO books (title, published_date, author_id, genre_id, editorial_id) VALUES (%s, %s, %s, %s, %s)', (title,published_date, author_id,genre_id,editorial_id))
        mysql.connection.commit()
        cursor.close()
        return {"message":"Book created successfully."}
    except Exception as e:
        print(f"Error creating book: {str(e)}")
        return {"message":"Error creating book"}

