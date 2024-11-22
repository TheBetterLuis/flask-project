from app import mysql

def get_users():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM users')
        columns = [column[0] for column in cursor.description]
        users = [dict(zip(columns,row)) for row in cursor.fetchall()]
        cursor.close()
        return users 
    except Exception as e:
        print(f"Error fetching users: {str(e)}")
        return {"error":"Failed to fetch users"}


#POST
def create_user(data):
    name = data.get('name')

    if not name:
        return {"message":"Must include user's name"}
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users (name) VALUES (%s)', (name,))
        mysql.connection.commit()
        cursor.close()
        return {"message":"user created successfully."}
    except Exception as e:
        print(f"Error creating user: {str(e)}")
        return {"message":"Error creating user"}
