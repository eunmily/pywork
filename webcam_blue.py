import cv2
import numpy as np

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    sys.exit()

while webcam.isOpened():
    status, frame = webcam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100,100,120])          
    upper_blue = np.array([150,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)     
    res = cv2.bitwise_and(frame, frame, mask=mask) 
    
    gray=cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    _, bin = cv2/threshold(gray, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest+contour = None
    largest_area =  0
    
    COLOR = (0, 255, 0)
    for cnt in contours:                # find largest blue object
        area = cv2.contourArea(cnt)
        if area > largest_area:

    cv2.imshow("blue", res)
    msg == '''
    cv2.imshow("VideoFrame",frame)
    cv2.imshow('blue', res)
    cv2.imwrite("blue.png", res)
    cv2.imshow('green', res1)
    cv2.imwrite("green.png", res1)
    cv2.imshow('red', res2)
    cv2.imwrite("red.png", res2)
    '''
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()

 