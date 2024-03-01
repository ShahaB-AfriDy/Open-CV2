import cv2.cv2 as cv2
from time import time
from Util import *
Video = cv2.VideoCapture(0)
# M = cv2.TrackerMIL_create()
Tracker  = cv2.TrackerMIL()

pTime = 0

while Video.isOpened():
    Success , img = Video.read()
    Flag , bbox = Tracker.update(img)

    if Flag:
        Draw_Box()
    else:
        cv2.putText(img, f'Lost', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (220, 0, 0), 2)


    cTime = time()
    fps = 1 / (cTime-pTime)
    pTime = cTime
    cv2.putText(img,f'fps: {int(fps)}',(20,80),cv2.FONT_HERSHEY_COMPLEX,2,(220,0,255),2)

    cv2.imshow('Video',img)
    if cv2.waitKey(1) == 27:
        break
