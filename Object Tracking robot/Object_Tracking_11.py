import cv2
from time import time
import Util

rect_size = 60
ptime = 0
deadzone = 100
cap,Ht,Wd,x_center,y_center = Util.Initial()
tolerance = 0.1
while True:
    _, frame2 = cap.read()
    red_mask,red = Util.Masking(frame2) # Masking
    Util.Countours(frame2, red_mask)  # countous
    cv2.line(frame2, (x_center-1,0), (x_center+1,Ht), (255, 255, 0), 3)
    cv2.line(frame2, (0,y_center-1),(Wd,y_center+1), (255, 255, 0), 3)
    cv2.rectangle(frame2,(x_center-rect_size,y_center-rect_size),(x_center+rect_size,y_center+rect_size),(0,0,255),3)


    ctime = time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(frame2,f'FPS: {int(fps)}',(30,60),cv2.FONT_HERSHEY_COMPLEX,1,(55,55,0),1)

    if Util.x_medium < (Wd//2)-deadzone:
        cv2.putText(frame2, f'Left', (x_center-50, Ht-50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
    elif Util.x_medium > (Wd//2)+deadzone:
        cv2.putText(frame2, f'Right', (x_center - 50, Ht - 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
    elif Util.y_medium < (Ht//2)-deadzone:
        cv2.putText(frame2, f'Forward', (x_center - 50, Ht - 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
    elif Util.y_medium > (Ht//2)+deadzone:
        cv2.putText(frame2, f'Backward', (x_center - 50, Ht - 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
    else:
        cv2.putText(frame2, f'Stop', (x_center - 50, Ht - 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)


    cv2.imshow("IN Frame", frame2)
    key = cv2.waitKey(1)
    if key == 27:
        print("key", key)
        break
cv2.destroyAllWindows()
cap.release()