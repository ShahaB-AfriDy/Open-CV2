import cv2
import Video_Stacking_1


cap = cv2.VideoCapture(0)

while True:
	Check,Frame = cap.read()
	Video_List = [[Frame,Frame,Frame]]
	Video = Video_Stacking_1.stackImages(scale=0.5,imgArray=Video_List)
	cv2.imshow('Video Frame',Video)

	if cv2.waitKey(1) == ord('q'):
		cap.release()
		cv2.destoryAllWindows()
		break