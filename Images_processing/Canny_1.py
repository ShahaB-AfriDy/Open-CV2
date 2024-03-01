# import cv2
# import numpy as np

# Image_Path = r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\Lane_Path.jpg'

# Image = cv2.imread(Image_Path)
# Image = cv2.resize(Image,(480,480))
# Canny = cv2.Canny(Image,200,700)

# cv2.imshow("Image Frame",Canny)
# cv2.waitKey(0)

# def funcCan(thresh1=0):
#     thresh1 = cv2.getTrackbarPos('thresh1', 'canny')
#     thresh2 = cv2.getTrackbarPos('thresh2', 'canny')
#     edge = cv2.Canny(img, thresh1, thresh2)
#     cv2.imshow('canny', edge)

# if __name__== '__main__':

#     original=cv2.imread(Image_Path,0)
#     original = cv2.resize(original,(480,480))
#     img=original.copy()
#     img=cv2.GaussianBlur(img,(5,5),0)

#     cv2.namedWindow('canny')

#     thresh1=100
#     thresh2=1
#     cv2.createTrackbar('thresh1','canny',thresh1,255,funcCan)
#     cv2.createTrackbar('thresh2','canny',thresh2,255,funcCan)
    
#     cv2.imshow('Frame',original)
#     funcCan(0)


#     cv2.waitKey(0)


# cv2.destroyAllWindows()

# import numpy as np
# import cv2


# video_capture = cv2.VideoCapture(0)
# video_capture.set(3, 160)
# video_capture.set(4, 120)

# while(True):

#     # Capture the frames
#     ret, frame = video_capture.read()

#     # Crop the image
#     crop_img = frame[60:120,0:160]

#     # Convert to grayscale
#     gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

#     # Gaussian blur
#     blur = cv2.GaussianBlur(gray,(5,5),0)

#     # Color thresholding
#     ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)

#     # Find the contours of the frame
#     contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

#     # Find the biggest contour (if detected)
#     if len(contours) > 0:
#         c = max(contours, key=cv2.contourArea)
#         # print("C ->: ",c)
#         M = cv2.moments(c)

#         cx = int(M['m10']/M['m00'])
#         cy = int(M['m01']/M['m00'])

#         cv2.line(crop_img,(cx,0),(cx,720),(255,0,0),2)
#         cv2.line(crop_img,(0,cy),(1280,cy),(255,0,0),2)

#         cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)

#         if cx >= 120:
#             print("Turn Left!: ",cx)

#         if cx < 120 and cx > 50:
#             print("On Track!: ",cx)

#         if cx <= 50:
#             print("Turn Right: ",cx)

#     else:
#         print("I don't see the line")

#     #Display the resulting frame
#     cv2.imshow('frame',crop_img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


