from heapq import nlargest
import cv2
import numpy as np
Image_Path = r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\Road_6.png'

def Get_Countours(Image,Image_Countour):
    List = []
    Countours,Hierarchy = cv2.findContours(Image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for countour in Countours:
        area = cv2.contourArea(countour)
        if area > 600:
            cv2.drawContours(Image_Countour,countour,-1,(255,0,255),5)

cv2.namedWindow('Threshod')
cv2.resizeWindow("Threshod",400,90)

def Empty(x):
    ...

cv2.createTrackbar("Lower","Threshod",0,255,Empty)
cv2.createTrackbar("Upper","Threshod",0,255,Empty)

# V = cv2.VideoCapture(0)
# V.set(3,300)
# V.set(4,200)
while True:
    # _,Image = V.read()
    # HSV = cv2.cvtColor(Image,cv2.COLOR_BGR2HSV)

    Image = cv2.imread(Image_Path)
    Image = cv2.resize(Image,(440,280))

    Image_countours = Image.copy()

    Image_Blur = cv2.GaussianBlur(Image,(7,7),0)
    Image_Gray = cv2.cvtColor(Image_Blur,cv2.COLOR_BGR2GRAY)

    lower = cv2.getTrackbarPos("Lower", "Threshod")
    upper = cv2.getTrackbarPos("Upper", "Threshod")
    # _,Th1 = cv2.threshold(Image,lower,upper,cv2.THRESH_BINARY)
    Image_Canny = cv2.Canny(Image_Gray,lower,upper)
    Image_Dilate = cv2.dilate(Image_Canny,np.ones((5,5),np.uint8),iterations=1)

    Get_Countours(Image_Dilate,Image_countours)

    # Lower = np.array([H_lower,S_lower,V_lower])
    # Upper = np.array([H_upper,S_upper,V_upper])
    # Lower = np.array([0,106,46])
    # Upper = np.array([255,255,255])
    # Mask = cv2.inRange(HSV,Lower,Upper)
    # Result = cv2.bitwise_and(Image,Image,mask = Mask)

    # cv2.imshow("Image",Image)
    # cv2.imshow("HSV", HSV)
    # cv2.imshow("Mask", Mask)
    # cv2.imshow("Result", Result)
    # cv2.imshow("Image",Image)
    cv2.imshow("Image Gray", Image_Gray)
    cv2.imshow("Image Canny", Image_Canny)
    cv2.imshow("Image Dilate", Image_Dilate)
    cv2.imshow("Image Countours", Image_countours)
    if cv2.waitKey(1) == ord('q'):
        # V.release()
        cv2.destroyAllWindows()
        break
