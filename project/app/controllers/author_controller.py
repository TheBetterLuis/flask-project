from app import mysql

def get_authors():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM authors')
        columns = [column[0] for column in cursor.description]
        authors = [dict(zip(columns,row)) for row in cursor.fetchall()]
        cursor.close()
        return authors 
    except Exception as e:
        print(f"Error fetching authors: {str(e)}")
        return {"error":"Failed to fetch authors"}


def create_author(data):
    author_name= data.get('name')

    if not author_name:
        return {"message":"must include author's name"}
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (%s)',(author_name,))
        mysql.connection.commit()
        cursor.close()
        return {"message":"author created successfully."}
    except Exception as e:
        print(f"Error creating author: {str(e)}")
        return {"message":"Error creating author"}
