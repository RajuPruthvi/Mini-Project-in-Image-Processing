import cv2
import numpy as np
import math

img = cv2.imread('images/img7.png', 1)

M = img.shape[0]
N = img.shape[1]
pixels = M*N

for k in np.arange(3) :
    hist = np.zeros(256)
    for i in np.arange(M) :
        for j in np.arange(N) :
            hist[img[i][j][k]] += 1
    for i in np.arange(1, 256) :
        hist[i] += hist[i-1]
    for i in np.arange(M) :
        for j in np.arange(N) :
            img[i][j][k] = math.floor(hist[img[i][j][k]] * 255 / pixels)

cv2.imwrite('images/img7_he.png', img)