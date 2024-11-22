from flask import Blueprint,jsonify,request

from app.controllers.review_controller import get_reviews,create_review

review = Blueprint('review',__name__)

#get
@review.route('/reviews',methods=['GET'])
def get_all_reviews():
    return jsonify(get_reviews())

#post
@review.route('/reviews',methods=['POST'])
def add_review():
    return jsonify(create_review(request.json))
