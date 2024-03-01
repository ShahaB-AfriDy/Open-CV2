import cv2
def Canny(Image):
    Gray = cv2.cvtColor(Image, cv2.COLOR_RGB2GRAY)
    Blur = cv2.GaussionBlur(Gray,(5,5),0)
    return  Blur
Image_Path = r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\Road_6.png'

Image = cv2.imread(Image_Path)
cv2.imshow("Image",Image)
cv2.imshow("Canny",Canny(Image.copy()))
cv2.waitKey(0)
#
