import tensorflow as tf 
import numpy as np 
import cv2
from backend.det import PersonDetector

print("Loading model...")
clf = PersonDetector()
print("Model loaded")

img = None
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Webcam',frame)

    #Wait to press 'q' key for capturing
    if cv2.waitKey(1) & 0xFF == ord('q'):
        img = frame
        cv2.destroyAllWindows()
        break

print("Received Image")

IMG_W = img.shape[1]
IMG_H = img.shape[0]
boxes,scores,classes,num = clf.get_classification(img)

persons = 0
for i in range(boxes.shape[1]):
    if scores[0][i] < 0.5 or classes[0][i] != 1:
        continue
    persons+=1
    best_box = boxes[0][i]
    cv2.rectangle(img,(int(best_box[1]*IMG_W),int(best_box[0]*IMG_H)),(int(best_box[3]*IMG_W),int(best_box[2]*IMG_H)),(0,255,0),3)

print("---------------------------")
print("{} Persons Detected".format(persons))

cv2.imwrite("cam.jpg",img)
cv2.imshow("IMG",img)
cv2.waitKey(0)