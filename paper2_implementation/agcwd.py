import cv2
import numpy as np
import math

img = cv2.imread('images/img7.png', 1)

M = img.shape[0]
N = img.shape[1]
pixels = M*N

alpha = 0.75

def agcwd(a) :
    F = np.zeros(256)

    for i in np.arange(M) :
        for j in np.arange(N) :
            F[a[i][j]] += 1

    F /= pixels

    pdfmax = 0
    pdfmin = 1
    for i in np.arange(256) :
        pdfmax = max(pdfmax, F[i])
        pdfmin = min(pdfmin, F[i])
    
    sum = 0.0
    for i in np.arange(256) :
        F[i] = pdfmax * pow( ((F[i] - pdfmin) / (pdfmax - pdfmin)) , alpha)
        sum += F[i]
    
    F /= sum

    for i in np.arange(1, 256) :
        F[i] += F[i-1]
    
    maxv = 0
    for i in np.arange(M) : 
        for j in np.arange(N) :
            maxv = max(maxv, a[i][j])

    new_values = np.zeros(256)
    for i in np.arange(256) : 
        new_values[i] = math.floor(maxv * pow(i/maxv, 1 - F[i]))

    for i in np.arange(M) : 
        for j in np.arange(N) :
            a[i][j] = new_values[a[i][j]]

    return a

for k in np.arange(3) :
    mat1 = np.zeros(shape = (M, N), dtype = int)
    for i in np.arange(M) :
        for j in np.arange(N) :
            mat1[i][j] = img[i][j][k]
    mat1 = agcwd(mat1)
    for i in np.arange(M) :
        for j in np.arange(N) :
            img[i][j][k] = mat1[i][j]

cv2.imwrite('images/img7_agcwd.png', img)