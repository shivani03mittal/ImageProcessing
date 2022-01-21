import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('IMG_2.jpg',0)
plt.imshow(img, cmap='gray'),plt.axis("off")
plt.show()

kernel = np.ones((9,9), np.uint8)
#closing
dilate = cv2.dilate(img,kernel,iterations = 3)
plt.imshow(dilate, cmap='gray'),plt.axis("off")
plt.show()
erosion = cv2.erode(dilate,kernel,iterations = 3)
plt.imshow(erosion, cmap='gray'),plt.axis("off")
plt.show()

dilate2 = cv2.dilate(erosion, kernel, iterations=2)
plt.imshow(dilate2, cmap='gray'), plt.axis("off")
plt.show()
erosion2 = cv2.erode(dilate2,kernel,iterations = 2)
plt.imshow(erosion2, cmap='gray'),plt.axis("off")
plt.show()


im = np.hstack((img,erosion2))
print("Image after performing closing:")
plt.imshow(im, cmap='gray')
plt.show()
