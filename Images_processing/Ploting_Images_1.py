import cv2
import numpy as np
from matplotlib import pyplot as plt

Image_Path = r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\NTS_2.png'

cv2.namedWindow('Threshod')
cv2.resizeWindow("Threshod",640,150)
def nothing(x):
	...

cv2.createTrackbar('hl','Threshod',40,480,nothing)
cv2.createTrackbar('hu','Threshod',20,480,nothing)
cv2.createTrackbar('wl','Threshod',40,640,nothing)
cv2.createTrackbar('wu','Threshod',20,640,nothing)



# img = cv2.imread(Image_Path,0)


while True:
	
	img = cv2.imread(Image_Path,0)
	img = cv2.resize(img,(640,480))

	H_L = cv2.getTrackbarPos("hl","Threshod")
	H_U = cv2.getTrackbarPos("hu","Threshod")
	W_L = cv2.getTrackbarPos('wl','Threshod')
	W_U = cv2.getTrackbarPos('wu','Threshod')
	

	img[H_L:H_U,W_L:W_U]

	cv2.imshow("Image",img)

	# _, th1 = cv2.threshold(img,Min, Max, cv2.THRESH_BINARY)
	# _, th2 = cv2.threshold(img, Min, Max, cv2.THRESH_BINARY_INV)
	# _, th3 = cv2.threshold(img, Min, Max, cv2.THRESH_TRUNC)
	# _, th4 = cv2.threshold(img, Min, Max, cv2.THRESH_TOZERO)
	# _, th5 = cv2.threshold(img, Min, Max, cv2.THRESH_TOZERO_INV)



	# cv2.imshow('Frame',np.hstack((img,th1,th2)))
	# cv2.imshow('Frame',np.hstack((img,th4,th5)))

	# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
	# images = [img, th1 ,th2 ,th3 ,th4, th5]

	# for i in range(6):
	#     plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
	#     plt.title(titles[i])
	#     plt.xticks([]),plt.yticks([])


	# plt.show()

	if cv2.waitKey(1) == ord('q'):
		cv2.destoryAllWindows()
		break