import cv2

img = cv2.imread("original.png", cv2.IMREAD_UNCHANGED)
while(1):
    cv2.imshow('title', img)
