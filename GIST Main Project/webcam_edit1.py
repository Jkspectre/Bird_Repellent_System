import cv2
import numpy as np
def drawOnFrames(img):
    x=150
    y= 100
    COLORS = np.random.uniform(0, 255, size=(1, 3))
    color= COLORS[0]
    #color= (0,255,0)
    rndFont = cv2.FONT_HERSHEY_SIMPLEX
    
    cv2.rectangle(img, (x,y), (x+70,y+90), color, 2)
    cv2.putText(img, 'Writing a text', (x-10,y-10), rndFont, .5, color, 2)
    return img





import cv2
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): 
    rval, frame = vc.read()
else:
    rval = False

while rval:
    frame = drawOnFrames(frame)
    frame = cv2.flip(frame,1)
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20) & 0xFF
    if key == 27 :
        break

vc.release()
cv2.destroyWindow("preview")

