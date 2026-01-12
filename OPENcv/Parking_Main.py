import cv2 as cv
import numpy as np
import cvzone
import pickle

weidth=107
height=48
cam=cv.VideoCapture("carPark.mp4")

try:
    with open("carparkpos","rb") as f:
        poslist=pickle.load(f)
except:
    poslist=[]


def checkParkingSpace(imgpors):
    spacecounter=0
    for pos in poslist:
        x,y=pos

        cropIMG=imgpors[y:y+height,x:x+weidth]
        count=cv.countNonZero(cropIMG)
        
        if count<900:
            color=(0,255,0)
            thickness=5
            spacecounter += 1
        else:
            color=(0,0,255)
            thickness=2
        
        cv.rectangle(img,pos,(pos[0]+weidth,pos[1]+height),color,thickness)
        cvzone.putTextRect(img,str(count),(x,y+height-3),scale=1,thickness=2,offset=0,colorR=color)


    cvzone.putTextRect(img,f'FREE SPACE: {spacecounter} / {len(poslist)}',(80,50),scale=3,thickness=3,offset=20,colorR=(0,200,0)) 


while True:
    success,img=cam.read()
    if cam.get(cv.CAP_PROP_POS_FRAMES) == cam.get(cv.CAP_PROP_FRAME_COUNT):
        cam.set(cv.CAP_PROP_POS_FRAMES,0)

    grayIMG=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    blurIMG=cv.GaussianBlur(grayIMG,(3,3),1)
    thresholdIMG=cv.adaptiveThreshold(blurIMG,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv.THRESH_BINARY_INV,25,16)
    medianblurIMG=cv.medianBlur(thresholdIMG,5)
    kernel=np.ones((3,3),np.int8)
    dilateIMG=cv.dilate(medianblurIMG,kernel,iterations=1)

    

    checkParkingSpace(dilateIMG)
  
       

    cv.imshow("Live",img)
    # cv.setMouseCallback("Live",mouseclick)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break