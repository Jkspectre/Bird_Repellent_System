import serial
import numpy as np
import cv2
import time

arduinodata = serial.Serial('com5',9600)
confidence_thr = 0.5
def arduino(startX, startY, endX, endY,idx):
    if idx == 3:
        finalX= (startX+endX)/2
        finalY= ((480-startY)+(480-endY))/2
        Xvalue= str(int(0.1875*finalX)+30)
        Yvalue= str(int(0.25*finalY)+30)
        arduinodata.write(Xvalue.encode())
        time.sleep(0.1)
        print(Xvalue.encode())
    

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
    "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

print("[INFO] loading model...")

shared_dir = '../../MobileNet-SSD/'
net = cv2.dnn.readNetFromCaffe(shared_dir+ 'deploy.prototxt' , shared_dir+ 'mobilenet_iter_73000.caffemodel')


blob=None
def applySSD(image):
    global blob
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

    net.setInput(blob)
    detections = net.forward()

    for i in np.arange(0, detections.shape[2]):

        confidence = detections[0, 0, i, 2]

        if confidence > confidence_thr:

            idx = int(detections[0, 0, i, 1])
            if idx != 3:
                continue;
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            
            arduino(startX, startY, endX, endY,idx)

            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
            
            cv2.rectangle(image, (startX, startY), (endX, endY),
                COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(image, label, (startX, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2,cv2.LINE_AA,False)
            return image
    return image



cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()
    (h, w) = frame.shape[0] , frame.shape[1]
else:
    rval = False

while rval:
    
    cv2.imshow("preview", frame)
    
    rval, frame = vc.read()
    frame = cv2.flip(frame,1)
    
    key = cv2.waitKey(20)
    if key == 27:
        break
    frame = applySSD(frame)
    
vc.release()
cv2.destroyWindow("preview")
