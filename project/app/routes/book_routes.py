from flask import Blueprint,jsonify,request

from app.controllers.book_controller import get_books,get_book,create_book,get_all

book = Blueprint('book',__name__)

#get
@book.route('/books',methods=['GET'])
def get_all_books():
    return jsonify(get_books())

@book.route('/books/all',methods=['GET'])
def get_all_data():
    return jsonify(get_all())

@book.route('/books/<book_id>',methods=['GET'])
def get_one_book(book_id):
    return jsonify(get_book(book_id))


#post

@book.route('/books',methods=['POST'])
def add_book():
    return jsonify(create_book(request.json))


