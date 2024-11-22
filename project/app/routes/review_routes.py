from flask import Blueprint,jsonify,request

from app.controllers.review_controller import get_reviews,create_review,update_review,delete_review,get_review

review = Blueprint('review',__name__)

#get
@review.route('/reviews',methods=['GET'])
def get_all_reviews():
    return jsonify(get_reviews())

@review.route('/reviews/<review_id>',methods=['GET'])
def get_one_review(review_id):
    return jsonify(get_review(review_id))

#post
@review.route('/reviews',methods=['POST'])
def add_review():
    return jsonify(create_review(request.json))

#patch
@review.route('/reviews/<review_id>',methods=['PATCH'])
def patch_review(review_id):
    return jsonify(update_review(review_id, request.json))

#delete
@review.route('/reviews/<review_id>',methods=['DELETE'])
def erase_review(review_id):
    return jsonify(delete_review(review_id))
