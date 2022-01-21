import cv2
import cv
from matplotlib import pyplot as plt
# 1.Reading and Displaying the Image
image = cv2.imread('v.jpeg')
togray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Kim Taehyung',image)
cv2.waitKey(0)
cv2.imshow('Kim Taehyung',togray)
cv2.waitKey(0)
backtorgb = cv2.cvtColor(togray, cv2.COLOR_GRAY2BGR)
cv2.imshow('Kim Taehyung',backtorgb)
color_img = cv2.cvtColor(togray, cv.CV_GRAY2RGB)
cv2.waitKey(0)
