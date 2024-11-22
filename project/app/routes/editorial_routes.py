from flask import Blueprint,jsonify,request

from app.controllers.editorial_controller import get_editorials,create_editorial,update_editorial,delete_editorial,get_editorial

editorial = Blueprint('editorial',__name__)

#get
@editorial.route('/editorials',methods=['GET'])
def get_all_editorials():
    return jsonify(get_editorials())

@editorial.route('/editorials/<editorial_id>',methods=['GET'])
def get_one_editorial(editorial_id):
    return jsonify(get_editorial(editorial_id))

#post
@editorial.route('/editorials',methods=['POST'])
def add_editorial():
    return jsonify(create_editorial(request.json))

#patch
@editorial.route('/editorials/<editorial_id>',methods=['PATCH'])
def patch_editorial(editorial_id):
    return jsonify(update_editorial(editorial_id, request.json))

#delete
@editorial.route('/editorials/<editorial_id>',methods=['DELETE'])
def erase_editorial(editorial_id):
    return jsonify(delete_editorial(editorial_id))
