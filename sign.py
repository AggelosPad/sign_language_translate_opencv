import cv2
import time
import random
import handtrack as htm
import findLetter as fl




pTime = 0
cTime = 0


cap = cv2.VideoCapture(0)
letter = ''


detector = htm.handDetector(detectionCon=0.75)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw = False)
    
    tipIds = [4, 8, 12, 16, 20] #mediapipe graph
    
    if len(lmList) != 0:
        
        fingers = []
        move = 'None'
        #Thumb check
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # 4 Fingers check 
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        totalFingers = fingers.count(1)
        letter = fl.findLetter(fingers,lmList)
        if letter:
            i =0 
            cv2.putText(img,letter, (250, 250), cv2.FONT_HERSHEY_PLAIN, 4,(255,0,0), 2)

    elif len(lmList) == 0 :

        cv2.putText(img,"Place your right hand on the screen", (50, 200), cv2.FONT_HERSHEY_PLAIN, 1,(255,0, 255), 2)
        
            
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    cv2.putText(img,"FPS: " + str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 2,(255, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

