import threading
import json
import requests

url="https://urlgoeshere.com"
payload = {"channel": "#test-notifications", "username": "jonbot", "text": "hi im jonbot and im helping chris learn python", "icon_emoji": ":jon:"}
headers = {'content-type': 'application/json'}

def jonbot():
    threading.Timer(3.0, jonbot).start()
    requests.post(url, data=json.dumps(payload), headers=headers)

jonbot()