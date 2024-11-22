from app import mysql

def get_editorials():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM editorials')
        columns = [column[0] for column in cursor.description]
        editorials = [dict(zip(columns,row)) for row in cursor.fetchall()]
        cursor.close()
        return editorials
    except Exception as e:
        print(f"Error fetching editorials: {str(e)}")
        return {"error":"Failed to fetch editorials"}


#POST
def create_editorial(data):
    editorial_name= data.get('name')

    if not editorial_name:
        return {"message":"must include editorial's name"}
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO editorials (name) VALUES (%s)', (editorial_name,))
        mysql.connection.commit()
        cursor.close()
        return {"message":"editorial created successfully."}
    except Exception as e:
        print(f"Error creating editorial: {str(e)}")
        return {"message":"Error creating editorial"}

