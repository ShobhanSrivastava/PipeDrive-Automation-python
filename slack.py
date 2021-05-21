import requests
import json

def send_slack_message(message):
    message_text = str(message)
    payload = { "text" : message_text }
    response = requests.post('https://hooks.slack.com/services/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',
                            data = json.dumps(payload))
    if response.status_code == 200:
        print("Slack Message Sent")
    else:
        print("Error sending message to slack")
        print(response.text)
    