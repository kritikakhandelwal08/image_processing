# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 21:42:02 2023

@author: my
"""

import cv2

vidcap = cv2.VideoCapture("C:\\Users\\my\\Downloads\\test1.mp4")
ret,image = vidcap.read()

count = 0
while True:
    if ret == True:
        cv2.imwrite("F:\\frame\\imgN%d.jpg"%count, image)
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        ret,image = vidcap.read()
        cv2.imshow("res",image)
        
        count += 1
        if cv2.waitKey(1) & 0xFF == ord("q"): 
            break
            cv2.destroyAllWindows()
vidcap.release()
cv2.destroyAllWindows()