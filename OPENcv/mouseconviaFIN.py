import cv2 as cv
import CVHandModule as chm
import math
import autopy
import numpy as np

camx=1340
camy=680
rframe=100
smoothing=7

plocx,plocy=0,0
clocx,clocy=0,0

cam=cv.VideoCapture(1)

cam.set(3,camx)
cam.set(4,camy)

scrw,scrh=autopy.screen.size()

detector=chm.HandDetection(detectioncon=0.8)


while True:
    success,img=cam.read()
    img=cv.flip(img, 1)
    
    img=detector.find_hand(img)
    lmlist=detector.find_position(img,draw=False)
    
    cv.rectangle(img,(rframe,rframe),(camx-rframe,camy-rframe),(0,255,0),3)
    if len(lmlist)!=0:
        x1,y1= lmlist[8][1],lmlist[8][2]
        x2,y2=lmlist[12][1],lmlist[12][2]
        distance=math.hypot(x2-x1,y2-y1)

        fings=detector.fingersup(lmlist)

        if fings[1]==1 and fings[2]==0:
            x3=np.interp(x1,(rframe,camx-rframe),(0,scrw))
            y3=np.interp(y1,(rframe,camy-rframe),(0,scrh))
            
            clocx = plocx + (x3 - plocx)/smoothing
            clocy = plocy + (y3 - plocy)/smoothing

            autopy.mouse.move(clocx,clocy)
            cv.circle(img,(x1,y1),15,(255,0,255),cv.FILLED)

            plocx,plocy=clocx,clocy
        
        if fings[1]==1 and fings[2]==1:
            if distance<40:
                cv.circle(img,(x1,y1),15,(0,255,0),cv.FILLED)
                cv.circle(img,(x2,y2),15,(0,255,0),cv.FILLED)
                autopy.mouse.click()


    cv.imshow("live",img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()


    
