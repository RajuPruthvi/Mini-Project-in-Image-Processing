import cv2
import numpy as np
import math

X = cv2.imread('images/img1.png', 0)
M = X.shape[0]
N = X.shape[1]

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
    return -0.5 + 1/(1 + math.exp(-(k-1)))

pixels = M*N
print(pixels)

hist = histogram(X)

f = np.zeros(256)
sum = 0.0

for i in np.arange(256) :
    f[i] = sigmoid(i)*(1 + hist[i])
    sum += f[i]

f /= sum

F = cumulative_histogram(f)

new_values = np.zeros(256)

for i in np.arange(256) :
    new_values[i] = math.floor(F[i] * 255)

Y = X.copy()

for i in np.arange(M) :
    for j in np.arange(N) : 
        a = X.item(i, j)
        # b = new_values[a]
        Y.itemset((i, j), new_values[a])

# print(Y)
# cv2.imwrite('images/img1_global_contrast.png', Y)
# f1 = open('x.txt', 'w')
# for i in np.arange(M) :
#     for j in np.arange(N) :
#         f1.write(str(X.item(i, j)) + '\n')

f2 = open('y_less1.txt', 'r')
for i in np.arange(M) :
    for j in np.arange(N) :
        tmp = f2.readline()
        Y.itemset((i, j), int(tmp))

cv2.imwrite('images/img1_local_enhance_less1.png', Y)