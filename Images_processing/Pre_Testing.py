import cv2
V = cv2.VideoCapture(0)

while V.isOpened():
    Checker,Frame = V.read()
    cv2.imshow("Frame",Frame)

    if cv2.waitKey(1) == ord('q'):
        break