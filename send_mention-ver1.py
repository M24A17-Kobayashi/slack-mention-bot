import os
from dotenv import load_dotenv
from slack_sdk.web import WebClient

#   token，user_id，尊信先のチャンネルをべた書きバージョン
load_dotenv()

SLACK_API_TOKEN = 'YOUR_SLACK_API_TOKEN'
USER_ID = 'YOUR_USER_ID'
CHANNEL_NAME = '#YOUR_CHANNEL_NAME'

client = WebClient(SLACK_API_TOKEN)
message = f"<@{USER_ID}>"
response = client.chat_postMessage(text=message, channel=CHANNEL_NAME)

print(response)