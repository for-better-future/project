import pickle
import cv2 as cv



weidth=107
height=48

try:
    with open('carparkpos','rb') as f:
        poslist=pickle.load(f)
except:
     poslist=[]

def mouseclick(events,x,y,flags,param):
    if events == cv.EVENT_LBUTTONDOWN:
        poslist.append((x,y))

    if events == cv.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(poslist):
            x1,y1=pos
            if x1<x<x1+weidth and y1<y<y1+height:
                poslist.pop(i)


    with open('carparkpos','wb') as f:
         pickle.dump(poslist,f)



while True:
    cam=cv.imread("parkingIMG.png")

    for pos in poslist:
        cv.rectangle(cam,pos,(pos[0]+weidth,pos[1]+height),(255,0,255),2)
        

    cv.imshow("live",cam)
    cv.setMouseCallback("live",mouseclick)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    

