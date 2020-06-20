import cv2
import numpy as np
import math

img = cv2.imread('images/lena.jpg', 0)

cv2.imwrite('images/lena_wcontrast.jpg', img)

h = img.shape[0]
w = img.shape[1]

mina = 255
maxa = 0

for i in np.arange(h) :
    for j in np.arange(w) :
        a = img.item(i, j)
        mina = min(mina, a)
        maxa = max(maxa, a)

print(mina, maxa)

for i in np.arange(h) :
    for j in np.arange(w) : 
        a = img.item(i, j)
        b = float(a-mina)/(maxa - mina) * 255
        img.itemset((i, j), b)

cv2.imwrite('images/lena_contrast.jpg', img)