import cv2
import numpy as np

cap = cv2.VideoCapture("test.mp4")
cap.set(3, 1280)
cap.set(4, 720)
out = cv2.VideoWriter("2.mp4", cv2.VideoWriter_fourcc(*"MJPG"), 10.0,(1280, 720))
i = 0
while True:
	ret, image = cap.read()#read the video frame
	if not ret:
		break
	out.write(image)
	cv2.imshow('demo',image)
	cv2.waitKey(10)
	print(i)
	i  = i + 1
cap.release()