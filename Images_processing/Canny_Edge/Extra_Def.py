import cv2
import numpy as np

def Canny_Image(Image):
    Gray = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
    Blur = cv2.GaussianBlur(Gray,(5,5),0)
    return cv2.Canny(Blur,50,150)
    # return Canny

def Region_Of_Interest(Image):
    Height = Image.shape[0]
    Polygons = np.array([[(200,Height),(1100,Height),(550,250)]])
    Mask = np.zeros_like(Image)
    cv2.fillPoly(Mask,Polygons,255)
    Masked_Image = cv2.bitwise_and(Image,Mask)
    return Masked_Image

def Display_Lines(Image,Lines):
    Lane_Image = np.zeros_like(Image)
    if Lines is not None:
        for x1,y1,x2,y2 in Lines:
            cv2.line(Lane_Image,(x1,y1),(x2,y2),(255,0,255),9)
    return Lane_Image

def Make_Coordinates(Image,Line_parameters):
    slope,intercept = Line_parameters
    y1 = Image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1-intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1,y1,x2,y2])

def Average_Slope_Intercept(Image,Lines):
    left_fit = []
    right_fit = []
    for line in Lines:
        x1,y1,x2,y2 = line.reshape(4)
        parameters  = np.polyfit((x1,x2),(y1,y2),1)
        slope = parameters[0]
        intercept = parameters[1]

        if slope < 0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))

    left_fit_average = np.average(left_fit,axis=0)
    right_fit_average = np.average(right_fit,axis=0)
    if len(left_fit) == 0:
        left_fit_average = [1,1]
    Left_Line = Make_Coordinates(Image,left_fit_average)
    Right_Line = Make_Coordinates(Image, right_fit_average)
    return np.array([Left_Line,Right_Line])
