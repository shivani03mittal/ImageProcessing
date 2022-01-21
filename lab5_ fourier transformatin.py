import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt,exp
#reading image

def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def gaussianLP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = exp(((-distance((y,x),center)**2)/(2*(D0**2))))
    return base

def gaussianHP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1 - exp(((-distance((y,x),center)**2)/(2*(D0**2))))
    return base



img = cv2.imread('Chess_Board.png',0)
cv2.imshow('Image',img)
cv2.waitKey(0)
plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)


f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
central= np.log(1+np.abs(fshift))

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(central , cmap= "gray")
plt.title("FFTOriginal"), plt.xticks([]), plt.yticks([])
plt.show()


#low pass filter
plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)
plt.subplot(131), plt.imshow(central , cmap= "gray")
plt.title("FFTOriginal"), plt.xticks([]), plt.yticks([])
LowPass = gaussianLP(50,img.shape)
plt.subplot(132), plt.imshow(LowPass, "gray"), plt.title("Gaussian Low Pass Filter")

LowPass1 = gaussianLP(50,central.shape)
plt.subplot(133), plt.imshow(LowPass1, "gray"), plt.title("OutputLow Pass Filter")

'''HighPass = gaussianHP(50,img.shape)
plt.subplot(133), plt.imshow(HighPass, "gray"), plt.title("Gaussian High Pass Filter")
'''
plt.show()

#passing fft
plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

plt.subplot(131), plt.imshow(central , cmap= "gray")
plt.title("FFTOriginal"), plt.xticks([]), plt.yticks([])


LowPass1 = gaussianLP(50,central.shape)
plt.subplot(132), plt.imshow(LowPass1, "gray"), plt.title("OutputLow Pass Filter")

HighPass1 = gaussianHP(50,central.shape)
plt.subplot(133), plt.imshow(HighPass1, "gray"), plt.title("Output High Pass Filter")

plt.show()
