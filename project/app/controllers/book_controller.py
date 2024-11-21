from app import mysql

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
        cursor.execute('INSERT into books (title,published_date,author_id,genre_id,editorial_id) VALUES (%s, %s, %s, %s, %s)')
        mysql.connection.commit()
        cursor.close()
        return {"message":"Book created successfully."}
    except Exception as e:
        print(f"Error creating book: {str(e)}")
        return {"message":"Error creating book"}

def create_author(data):
    author_name= data.get('name')

    if not author_name:
        return {"message":"must include author's name"}
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT into authors (name) VALUES (%s)')
        mysql.connection.commit()
        cursor.close()
        return {"message":"author created successfully."}
    except Exception as e:
        print(f"Error creating author: {str(e)}")
        return {"message":"Error creating author"}

