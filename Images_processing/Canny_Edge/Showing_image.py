import cv2
import numpy as np
from matplotlib import  pyplot as plt

Image_Path = r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\Road_7.jpg'

Image = cv2.imread(Image_Path)
# Image = cv2.resize(Image,(640,480))
Image = cv2.cvtColor(Image,cv2.COLOR_BGR2RGB)
plt.imshow(Image)
plt.show()
print("Finished")
