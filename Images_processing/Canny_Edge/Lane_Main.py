import cv2
import numpy as np
from matplotlib import  pyplot as plt
from Canny_Edge.Extra_Def import Canny_Image,Region_Of_Interest,Display_Lines,Average_Slope_Intercept
# Image_Path = r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\Road_7.jpg'

# Image = cv2.imread(Image_Path)
# # Image = cv2.resize(Image,(640,480))
# Lane_Image = np.copy(Image)
# Canny = Canny(Lane_Image)
# Crop_Image = Region_Of_Interest(Canny)
# Lines = cv2.HoughLinesP(Crop_Image,2,np.pi/180,100,np.array([]),minLineLength=60,maxLineGap=5)
#
# Average_Lines = Average_Slope_Intercept(Lane_Image,Lines)
# Lane_Image = Display_Lines(Lane_Image,Average_Lines)
# Combo_Image = cv2.addWeighted(Image,0.8,Lane_Image,1,1)
# plt.imshow(Combo_Image)
# plt.show()

Vid = cv2.VideoCapture(r'E:\Python in Sublime\Open_CV2\Images_processing\Canny_Edge\Testing22.mp4')
# Vid = cv2.VideoCapture('test2.mp4')
while Vid.isOpened():
    _,Frame = Vid.read()
    Canny_w = Canny_Image(Frame)
    Crop_Image = Region_Of_Interest(Canny_w)
    Lines = cv2.HoughLinesP(Crop_Image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
    Average_Lines = Average_Slope_Intercept(Frame,Lines)
    Lane_Image = Display_Lines(Frame,Average_Lines)
    Combo_Image = cv2.addWeighted(Frame,0.8,Lane_Image,1,1)
    cv2.imshow("Frame",Combo_Image)

    if cv2.waitKey(1) == ord('q'):
        Vid.release()
        cv2.destroyAllWindows()
        break






# Image_List = [Image,Canny(Image),Region_Of_Interest(Image)]
# Titles = ['Original','Canny',"ROI"]

# for u in range(3):
#     plt.subplot(1,3,u+1),plt.imshow(Image_List[u],'gray')
#     plt.title(Titles[u])
#     plt.xticks([]),plt.yticks([])
#
# plt.show()
# cv2.destroyAllWindows()