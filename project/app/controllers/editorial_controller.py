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

def get_editorial(id):
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM editorials WHERE id = %s',(id,))
        columns = [column[0] for column in cursor.description]
        response = dict(zip(columns,cursor.fetchone()))
        print(response)
        cursor.close()

        if response:
            return response
        else:
            return {"message":"Can't find editorial"}
    except Exception as e:
        print(f"Error fetching editorial: {str(e)}")
        return {"message":"Error fetching editorial"}       


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


#Patch
def update_editorial(id,data):
    name = data.get('name')

    if not name:
        return {"message":"Must include new editorial name"}
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE editorials SET name = %s WHERE id =%s', (name, id))
        mysql.connection.commit()
        cursor.close()
        return {"message":"editorial updated successfully."}
    except Exception as e:
        print(f"Error updating editorial: {str(e)}")
        return {"message":"Error updating editorial"}

#delete
def delete_editorial(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM editorials WHERE id = %s', (id,))
        mysql.connection.commit()
        cursor.close()
        return {"message":"Editorial deleted successfully."}
    except Exception as e:
        print(f"Error deleting editorial: {str(e)}")
        return {"message":"Error deleting editorial"}
