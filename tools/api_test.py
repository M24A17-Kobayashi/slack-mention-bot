from slack_sdk.web import WebClient

#   apiが利用できるか確認
client = WebClient()
response = client.api_test()

print(response)