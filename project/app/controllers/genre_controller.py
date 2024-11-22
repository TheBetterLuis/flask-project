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


