# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 12:48:30 2020

@author: dell
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/dell/Desktop/numbers/img.png') #input image

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img = cv2.resize(img,(512,512)) #resize the image

# plt.imshow(img)
# plt.show()

rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]]) #src points
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]]) #destination points

M = cv2.getPerspectiveTransform(pts1,pts2) #get the perspective transform
dst = cv2.warpPerspective(img,M,(300,300)) #apply the perspective transform

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
