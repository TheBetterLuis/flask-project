from flask import Blueprint,jsonify,request

from app.controllers.author_controller import get_authors,create_author

author = Blueprint('author',__name__)

#get
@author.route('/authors',methods=['GET'])
def get_all_authors():
    return jsonify(get_authors())

#post
@author.route('/authors',methods=['POST'])
def add_author():
    return jsonify(create_author(request.json))
