import datetime
from updater import updateStage
from duration import getDuration

def checkData(clientData):

    for data in clientData:
        dealID = data["id"]
        stageID = data["stage_id"]
        clientName = data["person_id"]["name"]
        print(f"Checking for {clientName} with deal ID : {dealID}")
        if stageID == 2 or stageID == 3:
            stageChangeTime = datetime.datetime.strptime(clientData[0]["stage_change_time"], "%Y-%m-%d %H:%M:%S")
            duration = getDuration(stageChangeTime)
            print(f"Deal has been in this stage for {duration} hours")
            if duration >= 48:
                print("Update Required")
                stageID = stageID+1
                print(f"Updating stage from {stage-1} to {stage}...")
                updateStage(dealID, stageID, clientName)
            else:
                print("Not completed 48 hours in the stage")
        else:
            print(f"Stage is {stageID}, Update not required")