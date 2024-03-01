import cv2
import numpy as np

# Black_Image = np.zeros((480,480,3),np.uint8)
Black_Image = cv2.imread(r'E:\Python in Sublime\Open_CV2\Images_processing\My_Images\Birthday.jpg')
Black_Image = cv2.resize(Black_Image, (640, 480))

# List = np.empty((4,2),dtype=np.int)
List = np.zeros((4,2),np.int)
counter = 0

def Clicking(event, x, y, parameter, flag):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        List[counter] = x,y
        counter += 1

def Get_Warp_Image(Black_Image):
    Width, Height = 250, 350
    Points_1 = np.float32([List[0], List[1], List[2], List[3]])
    Points_2 = np.float32([[0, 0], [Width, 0], [0, Height], [Width, Height]])
    matrix = cv2.getPerspectiveTransform(Points_1, Points_2)
    Bird_Eye_View = cv2.warpPerspective(Black_Image, M=matrix, dsize=(Width, Height))
    # for cropping the image
    Bird_Eye_View[30:320,30:220]
    cv2.imshow("Warp_Image", Bird_Eye_View)

while True:
    if counter == 4:
        Get_Warp_Image(Black_Image)
    if counter >=1 and counter < 4:
        for u in range(4):
            cv2.circle(Black_Image,(List[u][0],List[u][1]),5,(255,255,0),cv2.FILLED)
    cv2.imshow("Image", Black_Image)
    cv2.setMouseCallback('Image', Clicking)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break




# import RPi.GPIO as GPIO
# from picamera import PiCamera
# import time
# import cv2
# import numpy as np
# import math
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(7, GPIO.OUT)
# GPIO.setup(8, GPIO.OUT)
# theta=0
# minLineLength = 5
# maxLineGap = 10
# camera = PiCamera()
# camera.resolution = (640, 480)
# camera.framerate = 30
# rawCapture = PiRGBArray(camera, size=(640, 480))
# time.sleep(0.1)
# for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
#    image = frame.array
#    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#    edged = cv2.Canny(blurred, 85, 85)
#    lines = cv2.HoughLinesP(edged,1,np.pi/180,10,minLineLength,maxLineGap)
#    if(lines !=None):
#        for x in range(0, len(lines)):
#            for x1,y1,x2,y2 in lines[x]:
#                cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
#                theta=theta+math.atan2((y2-y1),(x2-x1))
#    #print(theta)GPIO pins were connected to arduino for servo steering control
#    threshold=6
#    if(theta>threshold):
#        GPIO.output(7,True)
#        GPIO.output(8,False)
#        print("left")
#    if(theta<-threshold):
#        GPIO.output(8,True)
#        GPIO.output(7,False)
#        print("right")
#    if(abs(theta)<threshold):
#       GPIO.output(8,False)
#       GPIO.output(7,False)
#       print("straight")
#    theta=0
#    cv2.imshow("Frame",image)
#    key = cv2.waitKey(1) & 0xFF
#    rawCapture.truncate(0)
#    if key == ord("q"):
#        break