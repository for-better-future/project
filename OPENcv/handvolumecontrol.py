import cv2 as cv
import numpy as np
import CVHandModule as chm
import math 
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

camx,camy=1840,780
cam=cv.VideoCapture(0)
cam.set(3,camx)
cam.set(4,camy)

detector=chm.HandDetection(detectioncon=0.7)



devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume=cast(interface, POINTER (IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
vol_range=volume.GetVolumeRange()

min_vol=vol_range[0]
max_vol=vol_range[1]
vol=0
percentage=400
per_text=0





while True:
    success,img=cam.read()
    
    img=detector.find_hand(img,)
    
    lmlist=detector.find_position(img,draw=False)
    # print(lmlist)
    if len(lmlist) != 0:
        x1,y1=lmlist[4][1],lmlist[4][2]
        x2,y2=lmlist[8][1],lmlist[8][2]
        c1,c2= (x1 + x2) // 2, (y1 + y2) // 2


        cv.circle(img,(x1,y1),10,(200,0,0),cv.FILLED)
        cv.circle(img,(x2,y2),10,(200,0,0),cv.FILLED)
       
        cv.line(img,(x1,y1),(x2,y2),(0,0,0),4)
        cv.circle(img,(c1,c2),10,(0,0,255),cv.FILLED)
    
        distance=math.hypot(x2-x1,y2-y1)
        
        
        if distance < 50 :
            cv.circle(img,(c1,c2),10,(0,255,0),cv.FILLED)

        #50-300

        vol=np.interp(distance,[30,330],[min_vol,max_vol])
        percentage=np.interp(distance,[30,330],[400,150])
        per_text=np.interp(distance,[30,330],[0,100])
        
        print(int(distance),vol)
        # print(vol)
        volume.SetMasterVolumeLevel(vol, None)

        cv.rectangle(img,(50,150 ),(85,400),(0, 140, 255),3)
        cv.rectangle(img,(50,int(percentage)),(85,400),(0, 140, 255),cv.FILLED)

        cv.putText(img,f'{int(per_text)}%',(40,450),cv.FONT_HERSHEY_SIMPLEX
                   ,1,(0, 140, 255),3)
        

    cv.imshow("live",img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()