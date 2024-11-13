import os
from dotenv import load_dotenv
from slack_sdk.web import WebClient

#   token，user_id，尊信先のチャンネルを.envから読み込むバージョン
load_dotenv()

SLACK_API_TOKEN = os.getenv('SLACK_API_TOKEN')
USER_ID = os.getenv('USER_ID')
CHANNEL_NAME = os.getenv('CHANNEL_NAME')

client = WebClient(SLACK_API_TOKEN)
message = f"<@{USER_ID}>"
response = client.chat_postMessage(text=message, channel=CHANNEL_NAME)

print(response)