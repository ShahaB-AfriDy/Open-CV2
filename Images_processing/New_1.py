import numpy as np
import cv2

Image_Path = r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\Lane_Path.jpg'


def empty():
	pass

cv2.namedWindow('Thresh')
thresh1=100
thresh2=1

cv2.resizeWindow("Thresh",640,240)
cv2.createTrackbar("Hue Min","Thresh",0,179,empty)
cv2.createTrackbar("Hue Max","Thresh",19,179,empty)
while True:

    img = cv2.imread(Image_Path,0)
    img = cv2.resize(img,(640,240))
    h_min = cv2.getTrackbarPos("Hue Min","Thresh")
    h_max = cv2.getTrackbarPos("Hue Max", "Thresh")
    blur = cv2.GaussianBlur(img,(5,5),0)
    ret,T = cv2.threshold(blur,h_min,h_max,cv2.THRESH_BINARY_INV)
    imgStack = np.hstack((img,T))
    cv2.imshow("Stacked Images", imgStack)

    cv2.waitKey(1)