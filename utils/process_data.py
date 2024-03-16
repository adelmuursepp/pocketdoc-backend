from google_sheets import read_google_sheet
from utils.get_database import get_database
from utils.fetch_recommendation import fetch_recommendation
from utils.fetch_urgency import fetch_urgency
from utils.save_admin_summary import save_admin_summary
import sys

def process_data():
    res = read_google_sheet()
    last_row = res[-1]
    time = last_row[0] # Retrieves the time col in table
    summary = last_row[3] # Retrieves the summary col in table
    name = last_row[1] # Retrieves the name col in table

    dbname = get_database()
    transcript_collection = dbname["transcript"]
    db_transcripts = list(transcript_collection.find())
    if len(db_transcripts) == 0:
        print('db transcripts is 0', db_trans)
        transcript_collection.insert_one({"time": time, "summary": summary})
    else:
        db_time = db_transcripts[0]["time"] # There should only be one transcript in array
        if (db_time != time):
            transcript_collection.delete_many({})
            transcript_collection.insert_one({"time": time, "summary": summary})
            print("DELETED AND UPDATED")

            recommendation_collection = dbname["recommendation"]
            recommendation_collection.delete_many({})
            recommendation_string = fetch_recommendation(summary)
            recommendation_collection.insert_one({"recc": recommendation_string})
            print("RECOMMENDATION UPDATED")

            urgency = fetch_urgency(summary)
            save_admin_summary(name, time, urgency, summary)
            print("URGENCY UPDATED")

            sys.stdout.flush()
        else:
            print("NO UPDATES")
            sys.stdout.flush()
