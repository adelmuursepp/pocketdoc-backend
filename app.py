from dotenv import load_dotenv
from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from google_sheets import read_google_sheet
from utils.process_data import process_data
from utils.get_database import get_database
from routes.recommended_actions_route import recommended_actions_route
from flask_cors import CORS
import sys

from utils.fetch_recommendation import fetch_recommendation

load_dotenv()

app = Flask(__name__)
CORS(app)
app.app_context().push()

app.register_blueprint(recommended_actions_route)

scheduler = BackgroundScheduler(daemon=True)

# Schedule the `check_google_sheets` function to run periodically
scheduler.add_job(process_data, 'interval', seconds=6, max_instances=2) 

@app.route('/')
def home():
    return "Hello, Flask with MongoDB!"

if __name__ == '__main__':
    dbname = get_database()
    print("Started the scheduler")
    sys.stdout.flush()
    scheduler.start()  # Start the scheduler
    sys.stdout.flush()
    try:
        app.run(use_reloader=False)  # Prevents the scheduler from being started twice in debug mode
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        scheduler.shutdown()