import tensorflow as tf 
import numpy as np 
import cv2
import json
from backend.det import PersonDetector

print("Loading model...")
clf = PersonDetector()
print("Model loaded")

bus_images = ["static/bus1.jpg","static/bus2.jpg","static/bus3.jpg","static/bus4.jpg"]
json_ids = ["bus1","bus2","bus3","bus4"]

persons_json = {}

for idx,img_name in enumerate(bus_images):
    img = cv2.imread(img_name,1)
    IMG_W = img.shape[1]
    IMG_H = img.shape[0]
    boxes,scores,classes,num = clf.get_classification(img)

    img_og = img.copy()

    persons = 0
    for i in range(boxes.shape[1]):
        if scores[0][i] < 0.5 or classes[0][i] != 1:
            continue
        persons+=1
        best_box = boxes[0][i]
        cv2.rectangle(img,(int(best_box[1]*IMG_W),int(best_box[0]*IMG_H)),(int(best_box[3]*IMG_W),int(best_box[2]*IMG_H)),(0,255,0),3)

    print("---------------------------")
    print("{} Persons Detected".format(persons))

    cv2.imshow("Original Image",img_og)
    cv2.waitKey(0)
    cv2.imshow("Detected",img)
    cv2.waitKey(0)

    cv2.imwrite(img_name[:11] + '_detected.jpg',img)

    persons_json[json_ids[idx]] = persons

print(persons_json)
with open('static/data.json','w') as file:
    json.dump(persons_json,file)