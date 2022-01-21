#Logical and arithmatic operations
import cv2
img1=cv2.imread('BW1.png',0)  #reading images
img2=cv2.imread('BW2.png',0)
cv2.imshow('Image1',img1)
cv2.waitKey(0)
cv2.imshow('Image2',img2)
cv2.waitKey(0)

#1st ouput
imgoutput1= img1 & img2  #bitwise and
cv2.imshow('output1',imgoutput1)
cv2.waitKey(0)

#2nd
imgoutput2= img1 | img2  #bitwise or
cv2.imshow('output2',imgoutput2)
cv2.waitKey(0)

#3rd
imgoutput3= img1 ^ img2  #bitwise Xor
cv2.imshow('output3',imgoutput3)
cv2.waitKey(0)

#4th
imgoutput4= ~img1   #bitwise NOT
cv2.imshow('output4',imgoutput4)
cv2.waitKey(0)

#5th
imgoutput5= ~img2   #bitwise NOT
cv2.imshow('output5',imgoutput5)
cv2.waitKey(0)

#second part
image1=cv2.imread('withoutme.jpg',0) # reading images
image2=cv2.imread('withme.jpg',0)
cv2.imshow('background',image1)
cv2.waitKey(0)
cv2.imshow('withme',image2)
cv2.waitKey(0)

resultimg= cv2.subtract(image1,image2)  # applying sub method , we can also use the basic (-) sign
cv2.imshow('output',resultimg)
cv2.waitKey(0)

eqimg1=cv2.equalizeHist(image1)
eqimg2=cv2.equalizeHist(image2)
cv2.imshow('equalized images',eqimg1)
cv2.waitKey(0)
cv2.imshow('equalized images',eqimg2)
cv2.waitKey(0)
resultimg2= cv2.subtract(eqimg1,eqimg2)  # applying sub method , we can also use the basic (-) sign
cv2.imshow('output',resultimg2)
cv2.waitKey(0)