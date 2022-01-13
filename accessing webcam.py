import cv2
#import numpy as np


#img = cv2.imread('sample.png')   #for reading a sample image
cap = cv2.VideoCapture(0)   #for accessing the camera
cap.set(3, 640)
cap.set(4, 480)

#for on qrcode to detect
#code = decode(img)
#print(code)

while True:

    ret, frame = cap.read()
    #for qrcode in decode(frame):
        #print(qrcode.data)  #for printing only the data of the code. we can also extract .rect
        #myData = qrcode.data.decode('utf-8')
        #print(myData)

    cv2.imshow('Result', frame)
    cv2.waitKey(1)