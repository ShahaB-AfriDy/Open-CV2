import numpy as np
import cv2

Image_Path = r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\Banana.jpg'
# cv2.imshow('Frame',Image)
# cv2.waitKey(0)

def nothing(x):
	pass

cv2.namedWindow("Circle")
cv2.resizeWindow("Circle",640,300)

cv2.createTrackbar('H_min','Circle',0,179,nothing)
cv2.createTrackbar('H_max','Circle',44,179,nothing)
cv2.createTrackbar('S_min','Circle',0,255,nothing)
cv2.createTrackbar('S_max','Circle',33,255,nothing)
cv2.createTrackbar('V_min','Circle',66,255,nothing)
cv2.createTrackbar('V_max','Circle',77,255,nothing)


while True:
	Image = cv2.imread(Image_Path)
	Image = cv2.resize(Image,(300,200))

	HSV = cv2.cvtColor(Image,cv2.COLOR_BGR2HSV)
	
	Hl = cv2.getTrackbarPos('H_min','Circle')
	Hu = cv2.getTrackbarPos('H_max','Circle')
	Sl = cv2.getTrackbarPos('S_min','Circle')
	Su = cv2.getTrackbarPos('S_max','Circle')
	Vl = cv2.getTrackbarPos('V_min','Circle')
	Vu = cv2.getTrackbarPos('V_max','Circle')

	Lower = np.array([Hl,Sl,Vl])
	Upper = np.array([Hu,Su,Vu])

	mask = cv2.inRange(HSV,Lower,Upper)
	Result = cv2.bitwise_and(Image,Image,mask=mask)

	Frame = np.hstack((Image,Result,HSV))
	cv2.imshow("Frame",Frame)

	if cv2.waitKey(1) == ord('q'):
		cv2.destroyAllWindows()
		break