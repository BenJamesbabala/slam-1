import numpy as np 
import cv2 as cv2 
from matplotlib import pyplot as plt 
import pygame

img = cv2.imread('ejemplo.jpg',0)
fast = cv2.FastFeatureDetector_create()

kp = fast.detect(img,None)
img2 = cv2.imread('ejemplo.jpg',0)
#cv2.drawKeypoints(img, kp, img2)
img2 = cv2.drawKeypoints(img, kp, img2)

cv2.imshow('final.png',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print ("todo okey") 