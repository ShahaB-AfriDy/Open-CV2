import cv2
from numpy import array
x_medium = 0
y_medium = 0
def Initial(Width=1200,Height=720):
    cap = cv2.VideoCapture(0)
    cap.set(3, Width)
    cap.set(4, Height)
    _, frame = cap.read()
    rows, cols, ch = frame.shape
    print(f'Row: {rows} Col: {cols}')
    return cap,rows,cols,int(cols/2),int(rows/2)


def Countours(Image,mask):
    global x_medium,y_medium
    contours_red, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours_red, key=lambda x:cv2.contourArea(x), reverse=True)
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(Image, (x , y) , (x + w, y + h) , (0, 255, 0), 2)
        x_medium = int((x + x + w) / 2) # int(x + (w/2))
        y_medium = int((y + y + h) / 2) # int(y + (h/2))
        print(f'x:  {x_medium} and y: {y_medium}')
        cv2.circle(Image, (x_medium, y_medium), 15, (250, 0, 0), -1)
        break

def Masking(Image):
    hsv_frame2 = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV)
    low_red = array([46, 126, 125])
    high_red = array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame2, low_red, high_red)
    red = cv2.bitwise_and(Image,Image, mask=red_mask)
    return red_mask,red
