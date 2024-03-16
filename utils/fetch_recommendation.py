from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

openai_api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=openai_api_key)

def fetch_recommendation(summary):
    response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": f"You are a medical assistant. Your task is to provide specific suggestions to heal and improve the health of the user with home remedies and potential adjustments in lifestyle, do NOT be generic. Use this information how user feels: {summary} When presented with the text, come up with a numbered list of 4 solutions, each solution being less than 20 words."},
  ])
    return response.choices[0].message.content
