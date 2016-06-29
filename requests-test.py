import json
import requests

url="https://urlgoeshere.com"
payload = {"channel": "#test-notifications", "username": "helothere", "text": "hi", "icon_emoji": ":shit:"}
headers = {'content-type': 'application/json'}

requests.post(url, data=json.dumps(payload), headers=headers)
