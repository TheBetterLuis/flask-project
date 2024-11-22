from flask import Blueprint,jsonify,request

from app.controllers.user_controller import get_users,create_user

user = Blueprint('user',__name__)

#get
@user.route('/users',methods=['GET'])
def get_all_users():
    return jsonify(get_users())

#post
@user.route('/users',methods=['POST'])
def add_user():
    return jsonify(create_user(request.json))
