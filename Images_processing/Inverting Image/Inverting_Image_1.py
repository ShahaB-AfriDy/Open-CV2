import cv2.cv2 as cv2
import  numpy as np

Image = cv2.imread('3.jpg')
Img = Image.copy()
y,x,_ = Image.shape

Img = Img[y//2:,:]

cv2.imshow('Image',Image)
cv2.imshow('Img',Img)
cv2.waitKey(0)