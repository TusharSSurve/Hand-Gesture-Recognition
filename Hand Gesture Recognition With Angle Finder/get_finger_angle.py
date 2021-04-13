import math 

def getAngle(b,c,a,flag=False):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    if flag==True:
        return round(ang + 360 if ang < 0 else ang)
    else:
        return round(ang)
    
def getDistance(p1,p2):
    return math.hypot(p1[0] - p2[0],p1[1] - p2[1])

def isThumbOpen(lmList):
    second = getAngle(lmList[2],lmList[1],lmList[3],True)
    third = getAngle(lmList[3],lmList[2],lmList[4],True)
    
    s_flag,t_flag = True,True
    if second>=210 and second<=265:
        s_flag = False
    if third>=195 and third<=265:
        t_flag = False
    return s_flag if s_flag==t_flag else t_flag

def isFingerOpen(lmList,s_range,e_range):
    f_angle = getAngle(lmList[1],lmList[0],lmList[2])
    
    f_flag = True
    if f_angle>=s_range and f_angle<=e_range:
        f_flag=False
    return f_flag

def isThumbNearIndexFinger(p1,p2):
    return getDistance(p1,p2) < 17

def simpleGesture(lmList):
    f_list = ['FIST!','ONE!','TWO!','THREE!','FOUR!','FIVE!']
    fingers = [isThumbOpen(lmList[0:5]),isFingerOpen(lmList[5:8],-10,160),isFingerOpen(lmList[9:12],-80,160),isFingerOpen(lmList[13:16],-70,160),isFingerOpen(lmList[17:20],-15,160)]
    if fingers[0]==False and fingers[1]==True and fingers[2]==False and fingers[3]==False and fingers[4]==True:
        return 'ROCK!'
    elif fingers[0]==True and fingers[1]==True and fingers[2]==False and fingers[3]==False and fingers[4]==True:
        return 'SPIDERMAN!'
    elif fingers[0]==False and fingers[1]==True and fingers[2]==True and fingers[3]==False and fingers[4]==False:
        return 'PEACE!'
    elif isThumbNearIndexFinger(lmList[4],lmList[8]) and fingers[0]==False and fingers[1]==False and fingers[2]==True and fingers[3]==True and fingers[4]==True:
        return 'OK!'
    else:
        return f_list[fingers.count(True)]
    
    