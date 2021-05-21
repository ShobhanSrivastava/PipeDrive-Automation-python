import requests
import json
from logic import checkData
from updater import deals_updated
from slack import send_slack_message

def lambda_handler(event, context):
    
    send_slack_message("Automation Triggered")

    url = 'https://ecbmedia.pipedrive.com/api/v1/deals?api_token=ebec4e865d5ad8750b80f50f742856c7d7e06c09'

    r = requests.get(url)

    if r.status_code == 200:
        print("Deals fetched")
        JSON = r.json()
        clientData = JSON["data"]
        print("Sending clientData for CHECK")
        checkData(clientData)
        
    
    print(f'Automation finished : {deals_updated} deals updated!')
    send_slack_message(f"Automation finished : {deals_updated} deals updated!")
        

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Successful",
            # "location": ip.text.replace("\n", "")
        }),
    }
