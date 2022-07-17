from gettext import find
from re import U
from sre_constants import SUCCESS
import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)
offset = 20
while True:
    ret, frame = cap.read()
    hands, img = detector.findHands(frame)
    if hands:
        hand = hands[0]
        im = detector.fingersUp(hand)
        lm = ["thumb", "index", "middle", "ring", "pinky"]
        ot = []
        if im[0] == 1:
            ot = 0
        if im[1] == 1:
            ot = 1
        if im[2] == 1:
            ot = 2
        if im[3] == 1:
            ot = 3
        if im[4] == 1:
            ot = 4
        print(lm[ot])
        
        x,y,w,h = hand['bbox']
        imgCrop = img[y-offset:y+h+offset, x-offset:x+w+offset]
        imS = cv2.resize(imgCrop, (265, 265))  
        cv2.imshow('img', imS)
        # find distance between hands
    if len(hands) == 2:
        hand1 = hands[0]
        hand2 = hands[1]
        x1,y1,w1,h1 = hand1['bbox']
        x2,y2,w2,h2 = hand2['bbox']
        dist = abs(x1-x2)
        print(dist)
        # if dist < 100:
        #     print('hands are close')
        # else:
        #     print('hands are far')
        cv2.line(img, (x1,y1), (x2,y2), (255, 0, 0), 3)
        
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()