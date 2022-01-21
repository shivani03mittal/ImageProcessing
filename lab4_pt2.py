import cv2
import numpy as np
import matplotlib.pyplot as plt
#reading image
img = cv2.imread('BalloonImage.png')
cv2.imshow('Image',img)
cv2.waitKey(0)

#function to plot multiple results

def plot_img (images, titles):
    fig, axs = plt.subplots(nrows=1, ncols= len(images), figsize= (20,20))
    for i,p in enumerate(images):
        axs[i].imshow(cv2.cvtColor(p, cv2.COLOR_BGR2RGB))
        axs[i].set_title(titles[i])

    plt.show()

#image sharpening

img  = cv2.filter2D(img,0,2)
cv2.imshow('smImage',img)
cv2.waitKey(0)

#to drew side by side comparision


for i in [1,3,5,7,9,11,13,15]:
    print("With kernel size: "+ str(i))

    #averaging filter
    avg_img= cv2.blur(img ,(i,i))

    #gaussian filter
    gaus_img= cv2.GaussianBlur(img,(i,i),0)

    #median filter
    median =cv2.medianBlur(img,i)

    #bilateral
    bi_img= cv2.bilateralFilter(img,i,255,255)

    images= [img,avg_img,gaus_img,median,bi_img]
    titles=["Original Image","Average (box filter)","gauusian filter",
            "Median filter","Bilateral filter"]

    plot_img(images, titles)


median = cv2.medianBlur(img,5)
cv2.imshow('Image',median)
cv2.waitKey(0)