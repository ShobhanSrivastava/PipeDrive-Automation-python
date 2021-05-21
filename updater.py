import requests
from slack import send_slack_message

deals_updated = 0

def updateStage(id, stage, name):
    
    messagelist = {
        
                "message1" : "Email 1 to Email 2",
                "message2" : "Email 2 to Email 3"
                
               }
               
    message = f"{name} Deal's stage updated from {messagelist[0] if (stage-1)==2 else messagelist[1]}"
    
    payload = {
                'stage_id': stage
              }
              
    print("Updating...")
    updateR = requests.put(
            f'https://ecbmedia.pipedrive.com/api/v1/deals/{id}?api_token=ebec4e865d5ad8750b80f50f742856c7d7e06c09', json=payload)
    print(updateR.status_code)
    
    if updateR.status_code == 200:
        deals_updated = deals_updated+1
        print(message)
        send_slack_message(message)
    else:
        print(f'Stage Update Unsuccessful for {name}')
        print(f'Error : updateR.text')
        send_slack_message(f'Stage Update Unsuccessful for {name} deal with {updateR.status_code} status !')