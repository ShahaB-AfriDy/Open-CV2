import cv2
import numpy as np
from time import time

cap = cv2.VideoCapture(0)
Ht = 700
Wd = 1200
rect_size = 60
ptime = 0
cap.set(3, Wd)
cap.set(4, Ht)
_, frame = cap.read()
rows, cols, ch = frame.shape
x_medium = int(cols / 2) #Initialize horizontal position
y_medium = int(rows / 2) #Initialize vertical positon

x_center = int(cols / 2) #Initialize Horizontal center position
y_center = int(rows / 2) #Initialize Vertical center position

v = 0
while True:
    _, frame2 = cap.read()
    hsv_frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
    low_red = np.array([46,126,125])
    high_red = np.array([179,255,255])
    red_mask = cv2.inRange(hsv_frame2,low_red,high_red)
    red = cv2.bitwise_and(frame2,frame2,mask=red_mask)
    #Contors
    contours_red, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours_red, key=lambda x:cv2.contourArea(x), reverse=True)
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame2, (x , y) , (x + w, y + h) , (0, 255, 0), 2)
        break
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        x_medium = int((x + x + w) / 2)
        y_medium = int((y + y + h) / 2)
        break
    # central line
    cv2.circle(frame2,(x_center,y_center),20,(250,0,0),3,cv2.FILLED)
        # vertical line
    cv2.line(frame2, (x_center,0), (x_center,Ht), (255, 255, 0), 3)
        # Horizontal line
    cv2.line(frame2, (0,y_center),(Wd,y_center), (255, 255, 0), 3)
    cv2.rectangle(frame2,(x_center-rect_size,y_center-rect_size),(x_center+rect_size,y_center+rect_size),(0,0,255),3)

    ctime = time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(frame2,f'FPS: {int(fps)}',(30,60),cv2.FONT_HERSHEY_COMPLEX,1,(55,55,0),1)

    cv2.imshow("IN Frame", frame2)
    key = cv2.waitKey(1)
    if key == 27:
        print("key", key)
        break
cv2.destroyAllWindows()
cap.release()