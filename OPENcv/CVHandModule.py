import cv2 as cv
import time
import mediapipe as mp

###########################################
#1.  hand detection
#2. hand possition 
###########################################

class HandDetection():
    def __init__(self,mode=False,hand_no=2,detectioncon=0.5,trackingcon=0.6):
        self.mode=mode
        self.hand_no=hand_no
        self.detectioncon=(detectioncon)
        self.trackingcon=(trackingcon)
        
        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(static_image_mode=self.mode,
                                      max_num_hands=self.hand_no,
                                      min_detection_confidence=float(self.detectioncon),
                                      min_tracking_confidence=float(self.trackingcon))
        self.mpDraw=mp.solutions.drawing_utils

    def find_hand(self,img,draw=True):
        
        imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.results=self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                  self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return img
    
    def find_position(self,img,handno=0,draw=True):
        lmlist=[]
    
        if self.results.multi_hand_landmarks:
             my_hand=self.results.multi_hand_landmarks[handno]
             for id ,Lm in enumerate(my_hand.landmark):
                        h,w,c=img.shape
                        cx,cy=int(Lm.x*w),int(Lm.y*h)
                       # print(id,cx,cy)
                        lmlist.append([id,cx,cy])
                        if draw:
                            cv.circle(img,(cx,cy),10,(150,25,200),cv.FILLED)           
        return lmlist
        
    def fingersup(self,lmlist=[]):
        fingers=[]
        self.lmlist=lmlist
        finTips=[4,8,12,16,20]
        self.finTips=finTips
        if self.lmlist[self.finTips[0]][1]<self.lmlist[self.finTips[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
             if self.lmlist[self.finTips[id]][2] < self.lmlist[self.finTips[id] - 2][2]:
                fingers.append(1)
             else:
                fingers.append(0)

        return fingers
    



  

def main():

    camW,camH= 1000,1000

    cam = cv.VideoCapture(1)
    cam.set(3,camW)
    cam.set(4,camH)
    detector=HandDetection()

    while True:
        success,img = cam.read()
        img=cv.flip(img, 1)
        img=detector.find_hand(img)
        lmlist=detector.find_position(img,draw=True)
        if len(lmlist) != 0:
           fings=detector.fingersup(lmlist)
           print(fings)


        cv.imshow("recording live",img)
    




        if cv.waitKey(1) & 0xFF == ord('q'):
           break

    cam.release()
    cv.destroyAllWindows()





if __name__ == "__main__" :
     main()
