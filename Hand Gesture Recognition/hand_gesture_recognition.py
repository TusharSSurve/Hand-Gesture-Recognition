import cv2 
import mediapipe as mp
from simple_gesture import simpleGesture

############## Initialization ##############
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands 
hands = mpHands.Hands(min_detection_confidence=0.80)
mpDraw = mp.solutions.drawing_utils

lms = [4,8,12,16,20]
############################################

while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []
    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for lm in handlandmark.landmark:
                h,w,_ = img.shape
                lmList.append([int(lm.x*w),int(lm.y*h)])
                
            mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)

    if lmList!=[]:
        fingers = []
        if lmList[0][1] < lmList[8][1]:
            cv2.putText(img,'Hand Gesture Not Recognisable!!',(20,50),cv2.FONT_HERSHEY_COMPLEX,0.9,(0,255,0),2)
        else:
            if lmList[5][0] < lmList[17][0]:
                fingers.append(True) if lmList[lms[0]][0] < lmList[lms[0]-2][0] else fingers.append(False)
            else:
                fingers.append(True) if lmList[lms[0]][0] > lmList[lms[0]-2][0] else fingers.append(False)

            for lm in range(1,len(lms)):
                fingers.append(True) if lmList[lms[lm]][1] < lmList[lms[lm]-2][1] else fingers.append(False)
                
            cv2.putText(img,simpleGesture(fingers,lmList[4],lmList[8]),(20,50),cv2.FONT_HERSHEY_COMPLEX,0.9,(0,255,0),2)
    
    
    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break