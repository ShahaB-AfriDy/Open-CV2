import cv2
import numpy as np

List = list()
counter = 0
def Clicking(event,x,y,parameter,flag):
    global  counter
    if event == cv2.EVENT_LBUTTONDOWN:
        List.append((x,y))
        counter+=1


Black = np.zeros((480,480,3),np.uint8)


while True:
    cv2.imshow("Image",Black)
    cv2.setMouseCallback('Image',Clicking)
    if len(List) >= 1:
        cv2.circle(Black,List[counter-1],20,(0,33,255),cv2.FILLED)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break