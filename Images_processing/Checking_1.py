
import cv2
import numpy as np
Image_Path = r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\White_Lane.jpg'

cv2.namedWindow('Threshod')
cv2.resizeWindow("Threshod",640,150)
def nothing(x):
	...

cv2.createTrackbar('Min','Threshod',40,255,nothing)
cv2.createTrackbar('Max','Threshod',20,255,nothing)


while True:
	img = cv2.imread(Image_Path,0)
	img = cv2.resize(img,(300,200))

	Min = cv2.getTrackbarPos("Min","Threshod")
	Max = cv2.getTrackbarPos("Max","Threshod")

	_, th1 = cv2.threshold(img,Min, Max, cv2.THRESH_BINARY)
	_, th2 = cv2.threshold(img, Min, Max, cv2.THRESH_BINARY_INV)
	_, th3 = cv2.threshold(img, Min, Max, cv2.THRESH_TRUNC)
	_, th4 = cv2.threshold(img, Min, Max, cv2.THRESH_TOZERO)
	_, th5 = cv2.threshold(img, Min, Max, cv2.THRESH_TOZERO_INV)


	cv2.imshow("Frame: 1",np.hstack((img,th1,th2)))
	cv2.imshow("Frame: 2",np.hstack((th3,th4,th5)))

	if cv2.waitKey(1) == ord('q'):
		cv2.destroyAllWindows()
		break