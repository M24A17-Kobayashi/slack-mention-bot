import os
from dotenv import load_dotenv
from slack_sdk.web import WebClient

def send():
    #   .envを有効化
    load_dotenv()

    #   .envからslack_api_token，user_id，送信先のチャンネル名を読み込み
    SLACK_API_TOKEN = os.getenv('SLACK_API_TOKEN')
    USER_ID = os.getenv('USER_ID')
    CHANNEL = os.getenv('CHANNEL_NAME')

    #   メンションを送信
    client = WebClient(SLACK_API_TOKEN)
    message = f"<@{USER_ID}>"
    response = client.chat_postMessage(text=message, channel=CHANNEL)

    print(response)