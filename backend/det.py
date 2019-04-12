import numpy as np
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt

class PersonDetector(object):
    def __init__(self):
        PATH_TO_MODEL = '/media/shreyas/Data/sct/project/SCT19/backend/model/frozen_inference_graph.pb'
        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            # Works up to here.
            with tf.gfile.GFile(PATH_TO_MODEL, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
            self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
            self.d_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
            self.d_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
            self.d_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
            self.num_d = self.detection_graph.get_tensor_by_name('num_detections:0')
        self.sess = tf.Session(graph=self.detection_graph)
    
    def get_classification(self, img):
        # Bounding Box Detection.
        with self.detection_graph.as_default():
            # Expand dimension since the model expects image to have shape [1, None, None, 3].
            img_expanded = np.expand_dims(img, axis=0)  
            (boxes, scores, classes, num) = self.sess.run(
                [self.d_boxes, self.d_scores, self.d_classes, self.num_d],
                feed_dict={self.image_tensor: img_expanded})
        return boxes, scores, classes, num

# TEST_IMG_NAME = '../images/2.jpg'
# img = cv2.imread(TEST_IMG_NAME)
# IMG_W = img.shape[1]
# IMG_H = img.shape[0]

# clf = PersonDetector()

# boxes,scores,classes,num = clf.get_classification(img)

# # Show the best bounding box
# img = cv2.imread(TEST_IMG_NAME)
# persons = 0
# for i in range(boxes.shape[1]):
#     if scores[0][i] < 0.5 or classes[0][i] != 1:
#         continue
#     persons+=1
#     best_box = boxes[0][i]
#     cv2.rectangle(img,(int(best_box[1]*IMG_W),int(best_box[0]*IMG_H)),(int(best_box[3]*IMG_W),int(best_box[2]*IMG_H)),(0,255,0),3)

# cv2.imshow("IMG",img)
# cv2.waitKey(0)