from app import mysql

def get_genres():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM genres')
        columns = [column[0] for column in cursor.description]
        genres = [dict(zip(columns,row)) for row in cursor.fetchall()]
        cursor.close()
        return genres 
    except Exception as e:
        print(f"Error fetching genres: {str(e)}")
        return {"error":"Failed to fetch genres"}

def get_genre(id):
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM genres WHERE id = %s',(id,))
        columns = [column[0] for column in cursor.description]
        response = dict(zip(columns,cursor.fetchone()))
        print(response)
        cursor.close()

        if response:
            return response
        else:
            return {"message":"Can't find genre"}
    except Exception as e:
        print(f"Error fetching genre: {str(e)}")
        return {"message":"Error fetching genre"}       


#POST
def create_genre(data):
    genre_name = data.get('name')

    if not genre_name:
        return {"message":"must include genre name"}
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO genres (name) VALUES (%s)', (genre_name,))
        mysql.connection.commit()
        cursor.close()
        return {"message":"genre created successfully."}
    except Exception as e:
        print(f"Error creating genre: {str(e)}")
        return {"message":"Error creating genre"}

#Patch
def update_genre(id,data):
    name = data.get('name')

    if not name:
        return {"message":"Must include new genre name"}
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE genres SET name = %s WHERE id =%s', (name, id))
        mysql.connection.commit()
        cursor.close()
        return {"message":"Genre updated successfully."}
    except Exception as e:
        print(f"Error updating author: {str(e)}")
        return {"message":"Error updating genre"}

#delete
def delete_genre(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM genres WHERE id = %s', (id,))
        mysql.connection.commit()
        cursor.close()
        return {"message":"Genre deleted successfully."}
    except Exception as e:
        print(f"Error deleting genre: {str(e)}")
        return {"message":"Error deleting genre"}
