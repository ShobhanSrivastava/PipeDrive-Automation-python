import datetime

def getDuration(then):
    now = datetime.datetime.now()
    difference = now - then
    seconds = difference.total_seconds()
    totalHours = seconds//3600
    return totalHours