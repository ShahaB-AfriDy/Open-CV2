
import cv2
import numpy as np
Image_Path = r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\Balls_2.jpg'
def Empty(x):
    ...

cv2.namedWindow('Threshod')
cv2.resizeWindow("Threshod",400,300)
cv2.createTrackbar("H_Lower","Threshod",0,179,Empty)
cv2.createTrackbar("H_Upper","Threshod",0,179,Empty)
cv2.createTrackbar("S_Lower","Threshod",0,255,Empty)
cv2.createTrackbar("S_Upper","Threshod",0,255,Empty)
cv2.createTrackbar("V_Lower","Threshod",0,255,Empty)
cv2.createTrackbar("V_Upper","Threshod",0,255,Empty)
V = cv2.VideoCapture(0)
V.set(3,300)
V.set(4,200)
while True:

    # Image = cv2.imread(Image_Path)
    # Image = cv2.resize(Image,(300,200))
    _,Image = V.read()
    HSV = cv2.cvtColor(Image,cv2.COLOR_BGR2HSV)

    H_lower = cv2.getTrackbarPos("H_Lower", "Threshod")
    H_upper = cv2.getTrackbarPos("H_Upper", "Threshod")
    S_lower = cv2.getTrackbarPos("S_Lower", "Threshod")
    S_upper = cv2.getTrackbarPos("S_Upper", "Threshod")
    V_lower = cv2.getTrackbarPos("V_Lower", "Threshod")
    V_upper = cv2.getTrackbarPos("V_Upper", "Threshod")

    # Lower = np.array([H_lower,S_lower,V_lower])
    # Upper = np.array([H_upper,S_upper,V_upper])
    Lower = np.array([0,106,46])
    Upper = np.array([255,255,255])

    Mask = cv2.inRange(HSV,Lower,Upper)
    Result = cv2.bitwise_and(Image,Image,mask = Mask)

    cv2.imshow("Image",Image)
    cv2.imshow("HSV", HSV)
    cv2.imshow("Mask", Mask)
    cv2.imshow("Result", Result)
    if cv2.waitKey(1) == ord('q'):
        V.release()
        cv2.destroyAllWindows()
        break
