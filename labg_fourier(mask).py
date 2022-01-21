import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve

#function to plot multiple results

def plot_img (images, titles):
    fig, axs = plt.subplots(nrows=1, ncols= len(images), figsize= (20,20))
    for i,p in enumerate(images):
        axs[i].imshow(p,cmap='gray')
        axs[i].set_title(titles[i])

    plt.show()
img = cv2.imread('Chess_Board.png',0)
#img_float32 = np.float32(img)
plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

fft = np.fft.fft2(img)
fshift = np.fft.fftshift(fft)
fft.shape
img.shape
print(fft.shape,img.shape)
central= 20*np.log(np.abs(fshift))

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(central , cmap= "gray")
plt.title("FFTOriginal"), plt.xticks([]), plt.yticks([])
plt.show()

rows, cols = img.shape
crow, ccol = rows//2 , cols//2     # center

# create low pass  mask first, center square is 1, remaining all zeros
mask_lp = np.zeros((rows, cols))
mask_lp[crow-300:crow+300, ccol-300:ccol+300] = 1

plt.imshow(mask_lp,cmap="gray")
plt.title('low pass filter mask'), plt.xticks([]), plt.yticks([])
plt.show()

# apply mask
fshift2 = cv2.filter2D(central,-1,mask_lp)
plt.imshow(fshift2,cmap="gray"),plt.title('LowOutput')
plt.show()

convolved_image_LP = fftconvolve(img,mask_lp)
plt.imshow(convolved_image_LP,cmap='gray'),plt.title('LowOutput')
plt.show()

#create high pass maks
mask_hp = np.ones((rows, cols))
mask_hp[crow-300:crow+300, ccol-300:ccol+300] = 0

plt.imshow(mask_hp,cmap="gray")
plt.title('high pass filter mask'), plt.xticks([]), plt.yticks([])
plt.show()

# apply hp mask
fshift3 = cv2.filter2D(central,-1,mask_hp)
plt.imshow(fshift3,cmap="gray"),plt.title('HighOutput')
plt.show()

convolved_image_HP = fftconvolve(img,mask_hp)
plt.imshow(convolved_image_HP,cmap='gray'),plt.title('HighOutput')
plt.show()


images= [img,central,convolved_image_LP,convolved_image_HP]
titles=["Original Image","OrginalFFT","LowOutput",
            "HighOutput"]

plot_img(images, titles)

