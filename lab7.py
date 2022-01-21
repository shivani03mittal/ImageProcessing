import cv2
import numpy as np
import matplotlib.pyplot as plt
image= cv2.imread('IMG_1.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)),plt.axis("off")
plt.show()

sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

sharpen_Image= cv2.filter2D(image,-1,sharpen_kernel)
plt.imshow(cv2.cvtColor(sharpen_Image, cv2.COLOR_BGR2RGB)),plt.axis("off")
plt.show()

kernel = np.ones((13,13), np.uint8)

image_new = cv2.morphologyEx(sharpen_Image, cv2.MORPH_CLOSE, kernel)
plt.imshow(cv2.cvtColor(image_new, cv2.COLOR_BGR2RGB)),plt.axis("off")
plt.show()

img = np.hstack((image,image_new))
print("Image after performing closing:")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()