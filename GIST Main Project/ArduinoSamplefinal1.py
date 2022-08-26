import serial
import time
import pyautogui

ar = serial.Serial('COM5',9600,timeout=1)
time.sleep(2)

def arduino(startX, startY, endX, endY):
    finalX= (startX+endX)/2
    finalY= ((400-startY)+(400-endY))/2
    Xvalue= str(int(0.24*finalX)+30)
    #Yvalue= str(int(0.3*finalY)+30)
    Xv= Xvalue.encode()
    #Yv=Yvalue.encode()
    ar.write(Xv)
    #ar.write(Yv)
    print(Xv,Yv)

while True:
    Xv,Yv = pyautogui.position();
    arduino(60,200,120,306)
    time.sleep(1);
    arduino(10,150,160,210)
    time.sleep(1);
    arduino(57,106,306,200)
    time.sleep(1);
    arduino(30,100,240,145)
    time.sleep(1);
    


