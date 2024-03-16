from flask import Blueprint, jsonify
from utils.get_database import get_database

recommended_actions_route = Blueprint('recommended_actions_route', __name__)

@recommended_actions_route.route('/recommended-actions')
def get_recommended_actions():
    dbname = get_database()
    recommendation_collection = dbname["recommendation"]
    db_recommendation = list(recommendation_collection.find())[0] # There should only be one recommendation in the array
    return jsonify({"recommendations": db_recommendation["recc"]})
