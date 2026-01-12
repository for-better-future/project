import cv2 as cv
import CVHandModule as chm
import numpy as np
import math


cam=cv.VideoCapture(1)
cam.set(3,1840)
cam.set(4,780)


detector=chm.HandDetection(detectioncon=0.8)

cx,cy,w,h=100,100,200,200
color=(255,0,0)

class Dragrect():
    def __init__(self,poscenter,size=[200,200]):
        self.poscenter=poscenter
        self.size=size

    def update(self,cursor):
        cx,cy=self.poscenter
        w,h=self.size 
        
        if cx-w//2<cursor[0]<cx+w//2 and cy-h//2<cursor[1]<cy+h//2: 
                 self.poscenter=cursor

rectlist=[]

for x in range(5):
    rectlist.append(Dragrect([x*250+150,150]))




while True:

    success,img=cam.read()
    img=cv.flip(img, 1)
    img=detector.find_hand(img)
    
    lmlist=detector.find_position(img,draw=False)
    if len(lmlist) != 0:  
        x1,y1= lmlist[8][1],lmlist[8][2]
        x2,y2=lmlist[12][1],lmlist[12][2]
        distance=math.hypot(x2-x1,y2-y1)

        print(distance)    
        if distance<50:
            cursor=lmlist[8][1],lmlist[8][2]
            for rect in rectlist:
                  rect.update(cursor)

    for rect in rectlist:
            cx,cy=rect.poscenter
            w,h=rect.size
            cv.rectangle(img,(cx-w//2,cy-h//2),(cx+w//2,cy+h//2),color,cv.FILLED) 



    cv.imshow("live",img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()