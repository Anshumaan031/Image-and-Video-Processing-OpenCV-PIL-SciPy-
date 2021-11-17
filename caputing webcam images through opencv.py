import cv2

cam = cv2.VideoCapture(0)      #capturing webcam

cv2.namedWindow("test")

img_counter = 0

while True:                 #for capturing each frame as images
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:      #if the esc key is pressed
        
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)    
        cv2.imwrite(img_name, frame)          #capturing the screenshot 
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()