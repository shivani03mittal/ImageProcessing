import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
import pandas as pd
image = cv2.imread('v.jpeg',0)

my_array = np.array(image)

print(my_array)
test_list = list(map(str,input().split()))
#test_list = ['This', 'is', 'Secret Code shhhh','by','Harshit','shivani']
arr = []
for ele in test_list:
    arr.extend(ord(num) for num in ele)
print(arr)
n  = len(arr)

for z in range(0,len(arr)):
    x = (z*2)+1
    y = (z*3)+2
    my_array[x][y]=arr[z]
my_array[0][0]=n
my_array

arr  =  my_array[:]
arr
cv2.imwrite('New_Encrypted_3.png',arr)

image_encrypted = cv2.imread('New_Encrypted_3.png',0)
plt.imshow(image_encrypted)
array = np.array(image_encrypted)
print(array)
lst = []
print("Code is:")
for i in range(0,array[0][0]):
    a = (i*2)+1
    b = (i*3)+2
    lst.append(array[a][b])
print(lst)

ASCII_values = lst[:]

ASCII_string = "".join([chr(value) for value in ASCII_values])

print(ASCII_string)

