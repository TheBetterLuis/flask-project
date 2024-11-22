from flask import Blueprint,jsonify,request

from app.controllers.genre_controller import get_genres,create_genre,get_genre,update_genre,delete_genre

genre = Blueprint('genre',__name__)

#get
@genre.route('/genres',methods=['GET'])
def get_all_genres():
    return jsonify(get_genres())

@genre.route('/genres/<genre_id>',methods=['GET'])
def get_one_genre(genre_id):
    return jsonify(get_genre(genre_id))

#post
@genre.route('/genres',methods=['POST'])
def add_genre():
    return jsonify(create_genre(request.json))

#patch
@genre.route('/genres/<genre_id>',methods=['PATCH'])
def patch_genre(genre_id):
    return jsonify(update_genre(genre_id, request.json))

#delete
@genre.route('/genres/<genre_id>',methods=['DELETE'])
def erase_genre(genre_id):
    return jsonify(delete_genre(genre_id))
