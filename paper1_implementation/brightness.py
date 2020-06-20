import cv2
import numpy as np
import math

img = cv2.imread('pruthvi.jpg', 0)

cv2.imwrite('lena_wcontrast.jpg', img)

h = img.shape[0]
w = img.shape[1]

threshold = 150

for i in np.arange(h) :
    for j in np.arange(w) :
        a = img.item(i, j)
        b = 0
        if(a > threshold) :
            b = 255
        img.itemset((i, j), b)

cv2.imwrite('lena_contrast.jpg', img)

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()