import math

def findLetter(fingers,lmList):
    letter = 'No'
    c = []
    totalFingers = fingers.count(1)
    tipIds = [4, 8, 12, 16, 20]
    
    if fingers[0]==1 and fingers[2]==0:
        letter = 'A'
    if fingers[0]==0 and totalFingers==4:
        letter = 'B'
    for id in range(1, 5):
            if  lmList[tipIds[id]][2] > lmList[tipIds[id] - 1][2]  and lmList[tipIds[id]][2] < lmList[tipIds[id] - 3][2]  :
            
                c.append(1)
            else:
                c.append(0)
    print(c,fingers)            
    if c.count(1) == 4:
        letter = 'C'    
    if fingers[1]== 1 and totalFingers == 1:
        letter = 'D'

    x0 ,y0 = lmList[4][1], lmList[4][2] #thumb tip
    x1 ,y1 = lmList[8][1], lmList[8][2]  #index finger tip
    x2 ,y2 = lmList[12][1], lmList[12][2] #middle finger tip
    x3 , y3 = lmList[6][1],lmList[6][2] #index funger pip

    distance01 = math.hypot(x1-x0,y1-y0)
    distance = math.hypot(x2-x1, y2-y1)
    distance1 = math.hypot(x3-x0,y3-y0)
    distance0 = math.hypot(x2-x0,y2-y0)
    #print(distance0)

    if fingers[1] == 0 and fingers[2] ==1 and fingers[3]==1 and fingers[4] ==1:
        letter ='F'

    if distance0 < 20 and c.count(1) == 4 and lmList[3][1] < lmList[4][1]:
        letter = 'E'



    if lmList[8][1] > lmList[5][1] and lmList[12][1] > lmList[9][1]:
        if lmList[16][1] < lmList[14][1] and lmList[20][1] < lmList[18][1]:
            letter = 'H'

    if lmList[8][1] > lmList[5][1] and lmList[4][1] > lmList[1][1] and fingers[0]==1 and totalFingers == 1:
        print(distance01)
        if distance01 > 50 and distance01 < 150:
            letter = 'G'

    if fingers[0] == 1 and fingers[4] == 1 and totalFingers ==2  and distance1 < 40:
            letter = 'I'        

    if lmList[20][1] > lmList[17][1] and fingers[4] == 1 and totalFingers==1:
            letter = 'J'

    if fingers[1]==1 and fingers[0]==1 and fingers[2]==1 and totalFingers==3:
            letter= 'K'

    if fingers[1] == 1 and fingers[0] == 1 and totalFingers == 2 :
        letter = 'L'

    if c.count(1)==3:
        letter = 'M'

    if c[0]==1 and c[1]==1  and c.count(1)==2:
        print("opaaaaaaaaaaa")
        letter = 'N'     

    if distance0 < 20 and c.count(1) == 4:
        letter = 'O'

    if fingers[1] == 1 and totalFingers == 1 and lmList[12][2] > lmList[9][2]:
        letter = 'P'

    if lmList[8][1] < lmList[12][1] and fingers[1] == 1 and fingers[2]==1 and totalFingers ==2:
        letter = 'R'

    if lmList[4][1] < lmList[6][1] and totalFingers == 1:
        if fingers[0] ==1 :
            letter = 'T'
       
    if fingers[1] == 1 and fingers[2] == 1 and totalFingers == 2 and distance < 25:
        if lmList[8][1] > lmList[12][1]:
            letter = 'U'

    if fingers[1]==1 and fingers[2]==1 and totalFingers == 2 and distance > 25:
       if c.count(1) !=0 :
        letter = 'V'

    if fingers[1]==1 and fingers[2]==1 and fingers[3] == 1  and totalFingers == 3:
        letter = 'W'

    if fingers[1]==1 and lmList[8][2] > lmList[7][2] and lmList[8][2] < lmList[6][2] and totalFingers==1:
        letter = 'X'

    if fingers[0] ==1 and fingers[4]==1 and totalFingers==2 and distance1 > 40:
        letter = 'Y'

    if fingers[1] == 1 and lmList[8][1] > lmList[5][1] and totalFingers ==1 :
        if lmList[12][1] < lmList[10][1]:
            letter= 'Z'

    if totalFingers==0 and c.count(1) == 0:
        letter = 'S'

    if letter != 'No':
        return letter

