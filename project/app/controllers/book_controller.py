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


def update_user2(id, data):
  # Obtener los datos enviados en la peticion
  if not data:
    return {"mensaje":"Debe enviarse los datos"}
  
  cursor = mysql.connection.cursor()
  
  update_query = "UPDATE users SET "
  update_data = []
  
  for campo, valor in data.items():
    if campo in ['nombre','apellido']:
      update_query += f"{campo} = %s, " # UPDATE users SET nombre = %s, 
      update_data.append(valor) # ["elimelech", "attale"]
      
  if not update_data:
    return {"mensaje":"Debe enviarse los datos"}
  
  # Vamos a eliminar la coma del final
  update_query = update_query.rstrip(", ")
  
  # Agregamos la condicion
  update_query += " WHERE id = %s" # UPDATE users SET nombre = %s WHERE id = %s
  
  update_data.append(id)
  
  # Ejecutamos la consulta
  cursor.execute(update_query, tuple(update_data,))
  
  mysql.connection.commit()
  cursor.close()
  
  return {"mensaje":"Usuario actualizado con exito"}

#Patch
def update_book(id,data):
    if not data:
        return {"message":"Must send new data"}

    cursor = mysql.connection.cursor()
    update_query = "UPDATE books SET "
    update_data = []
    for field, value in data.items():
        if field in ['title','published_date','author_id','genre_id','editorial_id']:
            update_query += f"{field} = %s, "
            update_data.append(value)
    if not update_data:
        return {"message":"Must send data"}
    update_query = update_query.rstrip(", ") 
    update_query += " WHERE id = %s"
    update_data.append(id)

    try:
        cursor.execute(update_query, tuple(update_data,))
        mysql.connection.commit()
        cursor.close()
        return {"message":"book updated successfully."}
    except Exception as e:
        print(f"Error updating book: {str(e)}")
        return {"message":"Error updating book"}

#delete
def delete_book(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM books WHERE id = %s', (id,))
        mysql.connection.commit()
        cursor.close()
        return {"message":"Book deleted successfully."}
    except Exception as e:
        print(f"Error deleting book: {str(e)}")
        return {"message":"Error deleting book"}

