import cv2
import numpy as np
from matplotlib import pyplot as plt

def Canny(Image):
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    Canny = cv2.Canny(blur, 50, 150)
    return  Canny
def Dilated(Image):
    Kernel = np.ones((7,7),np.uint8)
    Dilate = cv2.dilate(Image,Kernel)
    return Dilate
Black_Image = np.zeros((512,512,3),np.uint8)
Black_and_White = np.copy(Black_Image)
Black_and_White[:,Black_and_White.shape[1]//2:] = 255

# cv2.imshow("Black and White",Black_and_White)
cv2.imshow("Canny",Canny(Black_and_White))
cv2.imshow("Dilated",Dilated(Canny(Black_and_White)))
cv2.waitKey(0)