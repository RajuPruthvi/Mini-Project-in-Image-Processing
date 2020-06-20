import cv2
import numpy as np
import math

X = cv2.imread('images/img1_new.png', 0)
M = X.shape[0]
N = X.shape[1]

# cv2.imwrite('images/img1_gray.png', X)

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

print(Y)
# cv2.imwrite('images/img1_global_contrast.png', Y)

def ch(h) : 
    if h==0 :
        return math.sqrt(1/M)
    return math.sqrt(2/M)

def cw(w) : 
    if w==0 :
        return math.sqrt(1/N)
    return math.sqrt(2/N)

def dct(A) :
    B = A.copy()
    m = A.shape[0]
    n = A.shape[1]
    for h in np.arange(m) :
        for w in np.arange(n) :
            sum = 0.0
            for i in np.arange(m) :
                for j in np.arange(n) :
                    sum += A.item(i, j) * math.cos(math.pi*(2*i+1)*h/2*m)*math.cos(math.pi*(2*j+1)*w/2*n)
            B.itemset((h, w), ch(h)*cw(w)*sum)
    return B

def invdct(A) :
    B = A.copy()
    m = A.shape[0]
    n = A.shape[1]
    for h in np.arange(m) :
        for w in np.arange(n) :
            sum = 0.0
            for i in np.arange(m) :
                for j in np.arange(n) :
                    sum += ch(i)*cw(j)*A.item(i, j) * math.cos(math.pi*(2*i+1)*h/2*m)*math.cos(math.pi*(2*j+1)*w/2*n)
            B.itemset((h, w), sum)
    return B

D = dct(Y)

D2 = D.copy()

alpha = 1
for h in np.arange(M) :
    for w in np.arange(N) :
        if abs(D.item(h, w)) <= 0.01 * D.item(0, 0) :
            D2.itemset((h, w), alpha * D.item(h, w))

D2 = invdct(D2)
print(D2)

cv2.imwrite('images/img1_local_enhance.png', D2)