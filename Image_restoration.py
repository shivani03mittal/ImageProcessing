import numpy as np
import cv2
image = cv2.imread('Restore2.jpg')
mask = cv2.imread('mask.jpg',0)
cv2.imshow('Image_1',image)
cv2.waitKey(0)
cv2.imshow('mask',mask)
cv2.waitKey(0)
restored = cv2.inpaint(image,mask,10,cv2.INPAINT_TELEA)
a = np.hstack((image,restored))
restored_ns = cv2.inpaint(image,mask,10,cv2.INPAINT_NS)
b = np.hstack((image,restored_ns))
cv2.imshow('Orignal vs Restored',a)
cv2.waitKey(0)
cv2.imshow('Orignal vs Restored_ns',b)
cv2.waitKey(0)