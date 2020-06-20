import cv2
import numpy as np
import math

img = cv2.imread('images/img1.png', 0)

# cv2.imwrite('images/img1_gray.png', img)

def histogram(a) :
    h = a.shape[0]
    w = a.shape[1]
    ret = np.zeros(256)
    for i in np.arange(h) :
        for j in np.arange(w) :
            ret[a.item(i, j)] += 1
    return ret

def cumulative_histogram(a) :
    ret = np.zeros(256)
    ret[0] = a[0]
    for i in np.arange(1, 256) :
        ret[i] = ret[i-1] + a[i]
    return ret

h = img.shape[0]
w = img.shape[1]
pixels = h*w
# print(pixels)
# print(h, w)

hist = histogram(img)
cum_hist = cumulative_histogram(hist)

new_values = np.zeros(256)

for i in np.arange(256) :
    new_values[i] = math.floor(cum_hist[i] * 255.0 / pixels )

for i in np.arange(h) :
    for j in np.arange(w) : 
        a = img.item(i, j)
        b = new_values[a]
        img.itemset((i, j), b)

cv2.imwrite('images/img1_he.png', img)