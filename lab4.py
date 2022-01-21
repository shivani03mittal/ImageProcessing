import cv2
import numpy as np
import matplotlib.pyplot as plt
#reading image
img = cv2.imread('BalloonImage.png')
cv2.imshow('Image',img)
cv2.waitKey(0)

blur = cv2.blur(img,(7,7))
cv2.imshow('Image',blur)
cv2.waitKey(0)

gaussian = cv2.GaussianBlur(img,(11,11),0)
cv2.imshow('Image',gaussian)
cv2.waitKey(0)

median = cv2.medianBlur(img,5)
cv2.imshow('Image',median)
cv2.waitKey(0)

bilateral = cv2.bilateralFilter(img,15,200,30)
cv2.imshow('Image',bilateral)
cv2.waitKey(0)