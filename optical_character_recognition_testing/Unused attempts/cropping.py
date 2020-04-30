#import numpy as np
import cv2

image = cv2.imread('pearl_graph_inverted_jpg.jpg')
y=0
x=0
h=200
w=400
crop = image[y:y+h, x:x+w]
cv2.imshow('Image', crop)
cv2.waitKey(0) 


