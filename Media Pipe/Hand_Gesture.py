import mediapipe as mp
import cv2
import time
import math
import HandTrackingModule as htm

detector = htm.handDetector()

#00000000000000000000000000000000000000000000000000
Video = cv2.VideoCapture(0)
Video.set(3,640)
Video.set(4,480)
pTime = 0
# 00000000000000000000000000000000000000000000000000
TipID  = [4,8,12,16,20]
Looker = False
while True:
    checker , Frame = Video.read()
    Frame = detector.findHands(Frame,draw=False)
    lmList = detector.findPosition(Frame,draw=False)
    if len(lmList) != 0:
        Fingers = []
        if lmList[TipID[0]][1] > lmList[TipID[0]-1][1]:
            Fingers.append(1)
        else:
            Fingers.append(0)
        for lm in range(1,5):
            if lmList[TipID[lm]][2] < lmList[TipID[lm]-2][2]:
                Fingers.append(1)
            else:
                Fingers.append(0)

        Total_Fingers = Fingers.count(1)
        print(Total_Fingers)
        cv2.putText(Frame, str(int(Total_Fingers)), (250, 200), cv2.FONT_HERSHEY_PLAIN, 12,
                    (255, 0, 0), 7)


        # x0,y0 = lmList[0][1],lmList[0][2]
        # x4, y4 = lmList[4][1], lmList[4][2]
        # x8, y8 = lmList[8][1], lmList[8][2]
        # x12, y12 = lmList[12][1], lmList[12][2]
        # x16, y16 = lmList[16][1], lmList[16][2]
        # x20, y20 = lmList[20][1], lmList[20][2]
        # # circles
        # cv2.circle(Frame, (x0, y0), 4, (255, 0, 0), 8)
        # cv2.circle(Frame, (x4, y4), 4, (255, 0, 0), 8)
        # cv2.circle(Frame, (x8, y8), 4, (255, 0, 0), 8)
        # cv2.circle(Frame, (x12, y12), 4, (255, 0, 0), 8)
        # cv2.circle(Frame, (x16, y16), 4, (255, 0, 0), 8)
        # cv2.circle(Frame, (x20, y20), 4, (255, 0, 0), 8)
        # # lines
        # cv2.line(Frame, (x0, y0), (x4, y4), (0, 0, 0), 3)
        # cv2.line(Frame, (x0, y0), (x8, y8), (0, 0, 0), 3)
        # cv2.line(Frame, (x0, y0), (x12, y12), (0, 0, 0), 3)
        # cv2.line(Frame, (x0, y0), (x16, y16), (0, 0, 0), 3)
        # cv2.line(Frame, (x0, y0), (x20, y20), (0, 0, 0), 3)

        # for between circle
        # cx,cy = (x1+x2)//2,(y1+y2)//2
        # cv2.circle(Frame, (cx, cy), 4, (255, 0, 0), 8)
        #
        # Lenght = math.hypot(x2-x1,y2-y1)
        # # print(round(Lenght,2))
        # if Lenght < 60:
        #     cv2.circle(Frame, (cx, cy), 5, (255, 255, 255), 8)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(Frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Frame",Frame)
    if cv2.waitKey(1)==ord('q'):
        Video.release()
        cv2.destroyAllWindows()
        break
