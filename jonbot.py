import threading
import json
import requests

url = 'https://hooks.slack.com/services/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'
payload = {"channel": "#broforce", "username": "jonbot", "text": "hi im jonbot and im helping chris learn python", "icon_emoji": ":jon:"}
headers = {'content-type': 'application/json'}

def jonbot():
    threading.Timer(5.0, jonbot).start()
    requests.post(url, data=json.dumps(payload), headers=headers)

jonbot()