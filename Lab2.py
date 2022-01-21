import cv2
import matplotlib.pyplot as plt
import numpy as np
#reading image as grayscale (0)
img=cv2.imread('dark.jpg',0)
cv2.imshow('Image',img)
cv2.waitKey(0)
# shape of image
h,w= img.shape
print("Height Of image is :" ,h)
print("Width of image is:", w)

# histogram for original image
histogram = cv2.calcHist([img], [0], None, [256], [0, 256])

# show the plotting graph of an image
plt.plot(histogram)
plt.show()
#histogram equalization transformation
eq = cv2.equalizeHist(img)
#stacking image side by side
res = np.hstack((img,eq))
#comparision input and output image side-by-side
cv2.imshow('Equalized image',res)
cv2.waitKey(0)

#ploting the comparision
plt.hist(img.ravel(),256,[0,256]) #ploting input histo
plt.hist(eq.ravel(),256,[0,256]) #ploting input histo
plt.show()
cv2.waitKey(0)


#lograthimic transformation
c=255/(np.log(1 + np.max(img))) #transformation
#apply log transformation method
output=  np.log(img +1)*c

output= np.array(output, dtype= np.uint8) # int datatype
cv2.imshow('Log_Transformed.jpg',output) #showing image
cv2.waitKey(0)

#stacking image side by side
res = np.hstack((img,output))
#comparision input and output image side-by-side
cv2.imshow('Comparision of log  image',res)
cv2.waitKey(0)

#ploting the comparision
plt.hist(img.ravel(),256,[0,256]) #ploting input histo
plt.hist(output.ravel(),256,[0,256]) #ploting input histo
plt.show()

#ploting gray image
plt.imshow(img,cmap='gray')
plt.show()

#gama correction or power law transf.
#asking for gamma value
gvalue= float(input('Enter gamma value: '))
output=np.array(255*(img/255)** gvalue, dtype= np.uint8)
#show image
cv2.imshow("Gamma Transformation",output)
cv2.waitKey(0)

#stacking image side by side
res = np.hstack((img,output))
#comparision input and output image side-by-side
cv2.imshow('Comparision of power law trans. image',res)
cv2.waitKey(0)

#comparision
plt.hist(img.ravel(),256,[0,256])
plt.hist(output.ravel(),256,[0,256])
plt.show()



