import cv2
import numpy as np
import math

img = cv2.imread('images/img1.png', 0)
# print(img)
# cv2.imwrite('images/img1_gray.png', img)

def histogram(a) :
    ret = np.zeros(256)
    for i in np.arange(a.shape[0]) :
        for j in np.arange(a.shape[1]) :
            ret[a.item(i, j)] += 1
    return ret

def cumulative_histogram(a) :
    ret = np.zeros(256)
    ret[0] = a[0]
    for i in np.arange(1, 256) :
        ret[i] = ret[i-1] + a[i]
    return ret

def sigmoid(k) : 
    return -0.5 + (1/(1 + math.exp(-k)))

h = img.shape[0]
w = img.shape[1]
pixels = h*w

hist = histogram(img)
# print(hist)

f = np.zeros(256)
sum = 0.0

for i in np.arange(256) :
    f[i] = sigmoid(i)*(1 + hist[i])
    sum += f[i]
# print(sum)
# print(f)
f /= sum
# print(f)
F = cumulative_histogram(f)
# print(F)

new_values = np.zeros(256)

for i in np.arange(256) :
    new_values[i] = math.floor(F[i] * 255)

for i in np.arange(h) :
    for j in np.arange(w) : 
        a = img.item(i, j)
        b = new_values[a]
        if(b < 0) :
            b = 0
        if(b > 255) :
            b = 255
        img.itemset((i, j), b)

# print(img)
cv2.imwrite('images/img1_global_contrast.png', img)