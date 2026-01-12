import cv2 as cv
import time
import mediapipe as mp

###########################################
#1.  hand detection
#2. hand possition 
###########################################


camW,camH= 1000,1000

cam = cv.VideoCapture(0)
cam.set(3,camW)
cam.set(4,camH)


mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils




while True:
    success,img = cam.read()
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
              for id ,Lm in enumerate(handLms.landmark):
                 h,w,c=img.shape
                 cx,cy=int(Lm.x*w),int(Lm.y*h)
                 print(id,cx,cy)
                 if id==8:
                      cv.circle(img,(cx,cy),10,(150,25,200),cv.FILLED)
              
              
              mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

              
    
    
    cv.imshow("recording live",img)
    




    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()