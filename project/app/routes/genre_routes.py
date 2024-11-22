from flask import Blueprint,jsonify,request

from app.controllers.genre_controller import get_genres,create_genre

genre = Blueprint('genre',__name__)

#get
@genre.route('/genres',methods=['GET'])
def get_all_genres():
    return jsonify(get_genres())

#post
@genre.route('/genres',methods=['POST'])
def add_genre():
    return jsonify(create_genre(request.json))
