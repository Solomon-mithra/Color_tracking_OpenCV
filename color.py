import cv2
import numpy as np

def detect():
    pass

cap = cv2.VideoCapture(0);    
cv2.namedWindow("tracking")
cv2.createTrackbar("LH", "tracking",0,255,detect)
cv2.createTrackbar("Ls", "tracking",0,255,detect)
cv2.createTrackbar("Lv", "tracking",0,255,detect)
cv2.createTrackbar("UH", "tracking",255,255,detect)
cv2.createTrackbar("US", "tracking",255,255,detect)
cv2.createTrackbar("UV", "tracking",255,255,detect)


while True:
    #frame = cv2.imread("color-pic.jpeg")
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lh = cv2.getTrackbarPos("LH", "tracking")
    ls = cv2.getTrackbarPos("LS", "tracking")
    lv = cv2.getTrackbarPos("LV", "tracking")
    uh = cv2.getTrackbarPos("UH", "tracking")
    us = cv2.getTrackbarPos("US", "tracking")
    uv = cv2.getTrackbarPos("UV", "tracking")

    lb = np.array([lh, ls, lv])
    ub = np.array([uh, us, uv])
    
    mask = cv2.inRange(hsv, lb, ub)
    
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow("frame", frame)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break
        
cap.release()
csv.destroyAllWindows()
