import cv2 as cv

wcam , hcam = 800 , 600

cam=cv.VideoCapture(1)
cam.set(3,wcam)
cam.set(3,hcam)

framewidth=int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
frameheight=int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

codec = cv.VideoWriter_fourcc(*'mp4v')
recorder = cv.VideoWriter("myvid.mp4", codec, 20, (framewidth, frameheight))


while True:
    succ , image=cam.read()
    if not succ:
        break
    recorder.write(image)
    cv.imshow("recording live",image)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
recorder.release()
cv.destroyAllWindows()