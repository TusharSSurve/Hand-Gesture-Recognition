from math import hypot

def getDistance(p1,p2):
    return hypot(p1[0] - p2[0],p1[1] - p2[1])

def isThumbNearIndexFinger(p1,p2):
    return getDistance(p1,p2) < 20

def simpleGesture(fingers,p1,p2):
    f_list = ['FIST!','ONE!','TWO!','THREE!','FOUR!','FIVE!'] 
    if fingers[0]==False and fingers[1]==True and fingers[2]==False and fingers[3]==False and fingers[4]==True:
        return 'ROCK!'
    elif fingers[0]==True and fingers[1]==True and fingers[2]==False and fingers[3]==False and fingers[4]==True:
        return 'SPIDERMAN!'
    elif fingers[0]==False and fingers[1]==True and fingers[2]==True and fingers[3]==False and fingers[4]==False:
        return 'PEACE!'
    elif fingers[0]==True and fingers[1]==False and fingers[2]==False and fingers[3]==False and fingers[4]==True:
        return 'HANG LOOSE!'
    elif isThumbNearIndexFinger(p1,p2) and fingers[1]==False and fingers[2]==True and fingers[3]==True and fingers[4]==True:
        return 'OK!'
    else:
        return f_list[fingers.count(True)]