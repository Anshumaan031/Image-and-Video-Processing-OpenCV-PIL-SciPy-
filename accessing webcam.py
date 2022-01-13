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

    # Capture the video frame
    # by frame
    ret, frame = cap.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()