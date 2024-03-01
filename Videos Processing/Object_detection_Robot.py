import cv2 
import numpy as np

cap = cv2.VideoCapture(0)
Ht = 480
Wd = 640
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
    _, frame1 = cap.read()
    frame2 = cv2.flip(frame1,-1) # Flip image vertically
    frame2 = cv2.flip(frame1, 0) # flip image vertically
    hsv_frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
    # blurred_frame = cv2.GaussianBlur(frame1, (5, 5), 0)
    #blue Color
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
    # cv2.line(frame2, (x_medium, 0), (x_medium, (Ht)), (0, 255, 0), 2)
    # cv2.line(frame2, (0, y_medium), (Wd, y_medium), (0, 255, 0), 2)
    cv2.line(frame2, (320,y_medium), (x_medium,y_medium), (0, 255, 0), 2)
    cv2.line(frame2, (320, 0), (320,480), (255, 255, 0), 3)
    cv2.imshow("IN Frame", frame2)

    if x_medium < 320:
        v = ((x_medium*0.1)//2) - 15
    elif  290 >= x_medium <= 310:
        v = 0
    elif x_medium > 320:
        v = ((((640-x_medium)*0.1)//2) - 15) * -1
    print(v*0.03)
    key = cv2.waitKey(1)
    if key == 27:
        print("key", key)    
        break
cv2.destroyAllWindows()
cap.release()