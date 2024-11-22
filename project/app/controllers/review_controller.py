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

