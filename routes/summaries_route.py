from flask import Blueprint, jsonify
from utils.get_database import get_database

summaries_route = Blueprint('summaries_route', __name__)

@summaries_route.route('/summaries')
def get_summaries():
    dbname = get_database()
    summaries_collection = dbname["transcript"]
    # db_summaries = list(summaries_collection.find())[0] # There should only be one recommendation in the array
    
    all_summaries = []
    for summary in summaries_collection.find():
        all_summaries.append(summary)  
    return jsonify({"summaries": all_summaries})
