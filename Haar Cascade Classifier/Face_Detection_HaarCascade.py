import cv2

# Hr = cv2.CascadeClassifier("Stop_sign.xml")
Hr = cv2.CascadeClassifier("Traffic.xml")


Video = cv2.VideoCapture(0)
Video.set(3,320)
Video.set(4,240)

while Video.isOpened():
	Checker,Frame = Video.read()
	gray = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
	Scanners = Hr.detectMultiScale(gray,1.3,5)
	for (x,y,w,h) in Scanners:
		print("Stop Sign")
		print("Detected x,y",(x,y))
		print("Detected w,h",(w,h))

	cv2.imshow("Vidoe",Frame)
	if cv2.waitKey(1) == ord('q'):
		Video.release()
		cv2.destroyAllWindows()
		break
