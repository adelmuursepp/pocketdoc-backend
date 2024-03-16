from flask import Blueprint, jsonify
from utils.get_database import get_database

admin_summary_route = Blueprint('admin_summary_route', __name__)

@admin_summary_route.route('/admin-summary')
def get_recommended_actions():
    dbname = get_database()
    admin_summary_collection = dbname["adminsummary"]
    db_admin_summaries = admin_summary_collection.find().sort([("_id", -1)]).limit(3) 
    db_admin_summaries_array = (list(db_admin_summaries))
    res = []
    for obj in db_admin_summaries_array:
        new_obj = {
            "name": obj["name"],
            "time": obj["time"],
            "urgency": obj["urgency"],
            "summary": obj["summary"]
        }
        res.append(new_obj)
    return jsonify(res)
