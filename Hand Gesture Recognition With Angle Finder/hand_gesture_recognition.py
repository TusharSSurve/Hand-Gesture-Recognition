import cv2 
import mediapipe as mp 
from get_finger_angle import isThumbOpen,isFingerOpen,simpleGesture

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands 
hands = mpHands.Hands(min_detection_confidence=0.80)
mpDraw = mp.solutions.drawing_utils
drawSpecs = mpDraw.DrawingSpec(thickness=1,circle_radius=1)
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
                
            mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS,drawSpecs,drawSpecs)
    if lmList!=[]:
        cv2.putText(img,simpleGesture(lmList),(20,50),cv2.FONT_HERSHEY_COMPLEX,0.9,(0,255,0),2)
        
    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

#* 5 8 Index
#* 9 12 Middle
#* 13 16 Ring
#* 17 20 Pinky