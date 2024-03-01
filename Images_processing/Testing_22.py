import cv2
import numpy as np

# def getContours(img):

#     contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         print(area)
#         if area>500:
#             cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)

path = r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\Curve.jpg'

img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
# getContours(imgCanny)

cv2.imshow("Stack", imgStack)

cv2.waitKey(0)