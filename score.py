import time
bonus=0
def set_bonus(endtime,starttime):
    global bonus
    if 60>(endtime-starttime):
        bonus=60-round(endtime-starttime)
    else:
        bonus=0
    return bonus


