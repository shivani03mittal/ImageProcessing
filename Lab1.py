import cv2
from matplotlib import pyplot as plt
# 1.Reading and Displaying the Image
image = cv2.imread('v.jpeg')
cv2.imshow('Kim Taehyung',image)
cv2.waitKey(0) #will display the window infinitely until any keypress
#2 ii.	Know the dimension of an image
h,w,c= image.shape
print("Height Of image is :" ,h)
print("Width of image is:", w)
print("Channel if image is",c)

#3 iii.	Know the pixel intensities inside a ROI and at specific locations
ROI =image[110:190, 110:198]
print("Pixel intensity at ROI is :")
print(ROI)

specific_location=image[150,150]
print("the pixel intensities inside a ROI and at specific locations is:",specific_location)

#4iv.	Cropping the Image and Changing the size of an image
crop_image =image[0:171, 0:171]
cv2.imshow("Cropped Image",crop_image)
cv2.waitKey(0)

# resize
new_size= (int(w*0.5),int (h*0.5))
resized= cv2.resize(image,new_size)
cv2.imshow("resized",resized)
cv2.waitKey(0)

h,w,c=resized.shape
print("Height Of image is :" ,h)
print("Width of image is:", w)
print("Channel if image is",c)

#5 histogram
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# show the plotting graph of an image
plt.plot(histogram)
plt.show()