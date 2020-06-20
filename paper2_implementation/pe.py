import cv2
import numpy as np
import math

img = cv2.imread('images/img1.png', 1)

M = img.shape[0]
N = img.shape[1]
pixels = M*N

L = 10 
smin = 0
smax = 3

def pe(a) :
    F = np.zeros(256)

    for i in np.arange(M) :
        for j in np.arange(N) :
            F[a[i][j]] += 1

    for i in np.arange(1, 256) :
        F[i] += F[i-1]

    F /= pixels

    y = np.zeros(L+1)
    for i in np.arange(L+1) :
        y[i] = 255*i/L

    def Finv(z) :
        for i in np.arange(256) :
            if F[i] >= z :
                return i
        return 255

    x = np.zeros(L+1, dtype = int)
    for i in np.arange(L+1) :
        x[i] = Finv(y[i]/255)

    new_values = np.zeros(256)
    for k in np.arange(L) :
        mk = (y[k+1] - y[k])/(x[k+1] - x[k])
        if mk  < smin:
            mk = smin
        if mk > smax :
            mk = smax
        y[k+1] = y[k] + mk*(x[k+1] - x[k])
        for i in np.arange(x[k], x[k+1]) :
            new_values[i] = y[k] + mk*(i - x[k])

    for i in np.arange(M) :
        for j in np.arange(N) :
            a[i][j] = new_values[a[i][j]]

    return a

for k in np.arange(3) :
    mat1 = np.zeros(shape = (M, N), dtype = int)
    for i in np.arange(M) :
        for j in np.arange(N) :
            mat1[i][j] = img[i][j][k]
    mat1 = pe(mat1)
    for i in np.arange(M) :
        for j in np.arange(N) :
            img[i][j][k] = mat1[i][j]

cv2.imwrite('images/img1_pe.png', img)