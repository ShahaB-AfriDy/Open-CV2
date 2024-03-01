import cv2 as cv
import numpy as np
import Images_Stacking

Image_Path = r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\Lane_Path.jpg'

cv.nameWindow('Picker')
img = cv.imread(Image_Path,0)
img = cv.resize(img,(480,480))
blur = cv.GaussianBlur(img,(5,5),0)
ret,T = cv.threshold(blur,111,255,cv.THRESH_BINARY_INV)

_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)


# cv.imshow("Image", img)
# cv.imshow("th1", th1)
# cv.imshow("th2", th2)
# cv.imshow("th3", th3)
# cv.imshow("th4", th4)
# cv.imshow("th5", th5)
List_Frame = np.hstack((img,T))
cv.imshow("Frame",List_Frame)

cv.waitKey(0)
cv.destroyAllWindows()