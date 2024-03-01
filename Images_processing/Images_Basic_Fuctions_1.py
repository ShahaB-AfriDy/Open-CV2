import cv2
import numpy as np
import Images_Stacking_1

Image_Path = r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\Brandon.jpg'

Image = cv2.imread(Image_Path)
Gray = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
Blur = cv2.GaussianBlur(Gray,(21,21),3)
Canny = cv2.Canny(Image,450,300)

Images_List = [[Image,Gray,Blur],[Canny,Image,Image]]
Frame = Images_Stacking_1.stackImages(scale=0.1,imgArray=Images_List)

cv2.imshow("Image Frame",Frame)
cv2.waitKey(0)

