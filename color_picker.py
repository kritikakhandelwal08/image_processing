import cv2
import numpy as np

def cross(x):
    pass

img = np.zeros((300,512,3) , np.uint8)
cv2.namedWindow("Color picker")

s1 = "0:OFF\n1:ON"
cv2.createTrackbar(s1, "Color picker", 0,1, cross )

cv2.createTrackbar("R", "Color picker", 0,255, cross )
cv2.createTrackbar("G", "Color picker", 0,255, cross )
cv2.createTrackbar("B", "Color picker", 0,255, cross )

while True:
    cv2.imshow("Color picker", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    s = cv2.getTrackbarPos(s1, "Color picker")
    r = cv2.getTrackbarPos("R", "Color picker") 
    g = cv2.getTrackbarPos("G", "Color picker")
    b = cv2.getTrackbarPos("B", "Color picker")
    
    if s == 0:
        img[:] = 0
    else:
        img[:] = [r,g,b]
        
cv2.destroyAllWindows()