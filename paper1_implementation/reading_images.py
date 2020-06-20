import cv2

img = cv2.imread('lena.jpg', 0)

cv2.imshow('lenagray', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
cv2.imwrite('lena_gray.png', img)

