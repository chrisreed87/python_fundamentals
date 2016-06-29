import json
import requests

url="https://hooks.slack.com/services/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"
payload = {"channel": "#test-notifications", "username": "jonbot", "text": "hi im jonbot and im helping chris learn python", "icon_emoji": ":shit:"}
headers = {'content-type': 'application/json'}

requests.post(url, data=json.dumps(payload), headers=headers)
