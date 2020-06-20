import cv2
import numpy as np
import math

f = open('input.txt', 'w')

img = cv2.imread('images/img1.png', 0)

M = img.shape[0]
N = img.shape[1]

for i in np.arange(M) :
    for j in np.arange(N) :
        f.write(str(img.item(i, j)) + '\n')