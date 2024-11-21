from flask import Blueprint,jsonify,request

from app.controllers.book_controller import get_books,get_book,create_book,create_author

book = Blueprint('book',__name__)

@book.route('/books',methods=['GET'])
def get_all_books():
    return jsonify(get_books())

@book.route('/books/<book_id>',methods=['GET'])
def get_one_book(book_id):
    return jsonify(get_book(book_id))
