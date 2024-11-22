from app import mysql

def get_reviews():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM reviews')
        columns = [column[0] for column in cursor.description]
        reviews = [dict(zip(columns,row)) for row in cursor.fetchall()]
        cursor.close()
        return reviews 
    except Exception as e:
        print(f"Error fetching reviews: {str(e)}")
        return {"error":"Failed to fetch reviews"}


def get_review(id):
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM reviews WHERE id = %s',(id,))
        columns = [column[0] for column in cursor.description]
        response = dict(zip(columns,cursor.fetchone()))
        print(response)
        cursor.close()

        if response:
            return response
        else:
            return {"message":"Can't find review"}
    except Exception as e:
        print(f"Error fetching review: {str(e)}")
        return {"message":"Error fetching review"}       



#POST
def create_review(data):
    content = data.get('content')
    book_id = data.get('book_id')
    user_id = data.get('user_id')

    if not content or not book_id or not user_id:
        return {"message":"All fields are mandatory"}
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO reviews (content,book_id,user_id) VALUES (%s,%s,%s)', (content,book_id,user_id))
        mysql.connection.commit()
        cursor.close()
        return {"message":"review created successfully."}
    except Exception as e:
        print(f"Error creating genre: {str(e)}")
        return {"message":"Error creating review"}

#Patch
def update_review(id,data):
    if not data:
        return {"message":"Must send new data"}

    cursor = mysql.connection.cursor()
    update_query = "UPDATE reviews SET "
    update_data = []
#insert into reviews (content,book_id,user_id) values ("I love Harry Potter!",3,1);
    for field, value in data.items():
        if field in ['content','book_id','user_id']:
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
        return {"message":"review updated successfully."}
    except Exception as e:
        print(f"Error updating review: {str(e)}")
        return {"message":"Error updating review"}

#delete
def delete_review(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM reviews WHERE id = %s', (id,))
        mysql.connection.commit()
        cursor.close()
        return {"message":"Review deleted successfully."}
    except Exception as e:
        print(f"Error deleting review: {str(e)}")
        return {"message":"Error deleting review"}
