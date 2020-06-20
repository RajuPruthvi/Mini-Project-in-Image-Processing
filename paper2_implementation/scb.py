import cv2
import numpy as np
import math

img = cv2.imread('images/img7.png', 1)
M = img.shape[0]
N = img.shape[1]
pixels = M*N
print(pixels)

def scb(a) :
    hist = np.zeros(256)
    for i in np.arange(M) :
        for j in np.arange(N) :
            hist[a[i][j]] += 1
    for i in np.arange(1, 256) :
        hist[i] += hist[i-1]
    s1 = 0.5
    s2 = 0.5
    vmin = 0
    while hist[vmin+1] <= pixels*s1/100 : 
        vmin += 1
    vmax = 254
    while hist[vmax-1] > pixels*(1-s2/100) :
        vmax -=1 
    if vmax < 254 :
        vmax += 1
    for i in np.arange(M) :
        for j in np.arange(N) :
            if a[i][j] < vmin :
                a[i][j] = vmin
            if a[i][j] > vmax :
                a[i][j] = vmax
    for i in np.arange(M) :
        for j in np.arange(N) :
            a[i][j] = (a[i][j] - vmin) * 255 / (vmax - vmin)
    return a

matr = np.zeros(shape=(M, N), dtype = int)

for k in np.arange(3) :
    for i in np.arange(M) :
        for j in np.arange(N) :
            matr[i][j] = img[i][j][k]
    matr = scb(matr)
    for i in np.arange(M) :
        for j in np.arange(N) :
            img[i][j][k] = matr[i][j]

cv2.imwrite('images/img7_scb.png', img)