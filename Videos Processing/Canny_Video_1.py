import cv2

def funcCan(thresh1=0):
    thresh1 = cv2.getTrackbarPos('thresh1', 'canny')
    thresh2 = cv2.getTrackbarPos('thresh2', 'canny')
    edge = cv2.Canny(img, thresh1, thresh2)
    cv2.imshow('canny', edge)

cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,480)

cv2.namedWindow('canny')

thresh1=100
thresh2=1
cv2.createTrackbar('thresh1','canny',thresh1,255,funcCan)
cv2.createTrackbar('thresh2','canny',thresh2,255,funcCan)


if __name__== '__main__':
    while True:
        Checker,original=cap.read()
        # original = cv2.resize(original,(480,480))
        if Checker:
            img=original.copy()
            img=cv2.GaussianBlur(img,(5,5),0)
            funcCan(0)
            cv2.imshow('Frame',original)
            if cv2.waitKey(1) == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break