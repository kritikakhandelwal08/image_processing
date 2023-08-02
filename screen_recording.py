import cv2 as c
import pyautogui as p
import numpy as np

#create resolution
rs = p.size()


#filename in which we store ecording
fn = input("Please Enter any file name and path")
#fix the frame rate
fps = 60.0

fourcc = c.VideoWriter_fourcc(*"XVID")
output = c.VideoWriter(fn,fourcc,fps,rs)


#create recording module
c.namedWindow("Live_recording",c.WINDOW_NORMAL)
c.resizeWindow("live_recording", (600,400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = c.cvtColor(f, c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow("live_recording", f)
    k = c.waitKey(25)
    if k == ord("q") & 0xFF:
        break
    
output.release()
c.destroyAllWindows()