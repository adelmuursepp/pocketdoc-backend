from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

openai_api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=openai_api_key)

def fetch_urgency(summary):
    response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": f"Please classify the urgency of the following summary into one of the following categories: Low, Moderate, Urgent. Please only output the singular word. The summary is: {summary}"},
  ])
    return response.choices[0].message.content
