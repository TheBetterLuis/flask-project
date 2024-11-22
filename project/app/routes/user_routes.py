from flask import Blueprint,jsonify,request

from app.controllers.user_controller import get_users,create_user,update_user,delete_user

user = Blueprint('user',__name__)

#get
@user.route('/users',methods=['GET'])
def get_all_users():
    return jsonify(get_users())

#post
@user.route('/users',methods=['POST'])
def add_user():
    return jsonify(create_user(request.json))

#patch
@user.route('/users/<user_id>',methods=['PATCH'])
def patch_user(user_id):
    return jsonify(update_user(user_id, request.json))


#delete
@user.route('/users/<user_id>',methods=['DELETE'])
def erase_user(user_id):
    return jsonify(delete_user(user_id))


