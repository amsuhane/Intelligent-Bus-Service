import tensorflow as tf 
import numpy as np 
import cv2
import json
from backend.det import PersonDetector
import gps

img_name = "test.jpg"

print("Loading model...")
clf = PersonDetector()
print("Model loaded")

img = cv2.imread(img_name,1)
img_og = img.copy()

img = cv2.resize(img,(1024,725))
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

cv2.namedWindow("Original Image",cv2.WINDOW_NORMAL)
cv2.namedWindow("Detected",cv2.WINDOW_NORMAL)
cv2.imshow("Original Image",img_og)
cv2.waitKey(0)
cv2.imshow("Detected",img)
cv2.waitKey(0)

cv2.imwrite("custom_detected.jpg",img)

print("---------------------------")
print("Getting GPS Data")

gps.get_map_screenshot()