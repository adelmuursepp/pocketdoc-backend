from utils.get_database import get_database

def save_admin_summary(name, time, urgency, summary):
    dbname = get_database()
    admin_summary_collection = dbname["adminsummary"]
    admin_summary_collection.insert_one({"name": name, "time": time, "urgency": urgency, "summary": summary})
