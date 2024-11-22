from flask import Blueprint,jsonify,request

from app.controllers.editorial_controller import get_editorials,create_editorial

editorial = Blueprint('editorial',__name__)

#get
@editorial.route('/editorials',methods=['GET'])
def get_all_editorials():
    return jsonify(get_editorials())

#post
@editorial.route('/editorials',methods=['POST'])
def add_editorial():
    return jsonify(create_editorial(request.json))
