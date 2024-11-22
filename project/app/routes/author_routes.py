from flask import Blueprint,jsonify,request

from app.controllers.author_controller import get_authors,create_author,update_author,delete_author

author = Blueprint('author',__name__)

#get
@author.route('/authors',methods=['GET'])
def get_all_authors():
    return jsonify(get_authors())

#post
@author.route('/authors',methods=['POST'])
def add_author():
    return jsonify(create_author(request.json))

#patch
@author.route('/authors/<author_id>',methods=['PATCH'])
def patch_author(author_id):
    return jsonify(update_author(author_id, request.json))


#delete
@author.route('/authors/<author_id>',methods=['DELETE'])
def erase_author(author_id):
    return jsonify(delete_author(author_id))

