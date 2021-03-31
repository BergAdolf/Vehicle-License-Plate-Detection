import cv2
import numpy as np

cap = cv2.VideoCapture("output.avi")
cap.set(3, 1280)
cap.set(4, 720)
out = cv2.VideoWriter("output2.avi", cv2.VideoWriter_fourcc(*"MJPG"), 10.0,(1280, 720))
i  = 1
t = 0
while True:
	ret, image = cap.read()#read the video frame
	if not ret:
		break
	carplate = np.loadtxt('./carplate.txt',delimiter=',')
	car = np.loadtxt('./car.txt',delimiter=',')
	frame = car[:,0]
	if i in frame:
		xmin = int(car[t,2])
		ymin = int(car[t,3])
		pt1 = (int(carplate[t,0])+xmin,int(carplate[t,1])+ymin)
		pt2 = (int(carplate[t,2])+xmin,int(carplate[t,3])+ymin)
		cv2.rectangle(image,pt1,pt2, (0, 0, 255), 3)
		t = t + 1
	i = i + 1
	out.write(image)
cap.release()
