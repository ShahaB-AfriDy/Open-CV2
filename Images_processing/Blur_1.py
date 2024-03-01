
import cv2
import numpy as np
Image_Path = r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\Curve.jpg'

cv2.namedWindow('Threshod')
cv2.resizeWindow("Threshod",640,150)
def nothing(x):
	...

cv2.createTrackbar('Min','Threshod',40,255,nothing)
cv2.createTrackbar('Max','Threshod',255,255,nothing)


while True:
	img = cv2.imread(Image_Path)
	img = cv2.resize(img,(300,200))

	Min = cv2.getTrackbarPos("Min","Threshod")
	Max = cv2.getTrackbarPos("Max","Threshod")

	blur = cv2.GaussianBlur(img,(5,5),0)
	_, th1 = cv2.threshold(img,Min, Max, cv2.THRESH_BINARY)
	_, th2 = cv2.threshold(blur, Min, Max, cv2.THRESH_BINARY_INV)
	# contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	
	# _, th3 = cv2.threshold(img, Min, Max, cv2.THRESH_TRUNC)
	# _, th4 = cv2.threshold(img, Min, Max, cv2.THRESH_TOZERO)
	# _, th5 = cv2.threshold(img, Min, Max, cv2.THRESH_TOZERO_INV)

	# coutours, hierarchy = cv2.findContours(th2.copy(), 1, cv2.CHAIN_APPROX_NONE)
	# cv2.drawContours(img, contours, -1, (0,255,0), 1)
	th = cv2.cvtColor(th1,cv2.COLOR_RGB2BGR)
	cv2.imshow("Frame: 1",np.hstack((img,th,th2)))
	# cv2.imshow("Frame: 2",np.hstack((th3,th4,th5)))

	if cv2.waitKey(1) == ord('q'):
		cv2.destroyAllWindows()
		break