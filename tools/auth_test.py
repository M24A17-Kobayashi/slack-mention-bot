import os
from slack_sdk.web import WebClient

SLACK_API_TOKEN = "YOUR_SLACK_API_TOKEN"

#   authでトークンが有効か確認
client = WebClient(SLACK_API_TOKEN)
response = client.auth_test()

print(response)