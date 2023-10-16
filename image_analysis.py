import cv2
import numpy as np
img1 = cv2.imread('wro.jpg')
img = cv2.imread('green.jpg')
cv2.imshow('a', img)
cv2.imshow('b', img1)
print(type(img))
print(type(img1))

print(img1.shape)
print(img.shape)

for i in range(1080):
    for j in range(1920):
        if img[i][j][0] < 100 and img[i][j][1] > 100 and img[i][j][2] < 100:
            img[i][j][0] = img1[i][j][0]
            img[i][j][1] = img1[i][j][1]
            img[i][j][2] = img1[i][j][2]

cv2.imshow('b', img1)
cv2.imshow('TITLE', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
low_G = np.array([0, 100, 0]) # RGB
up_G = np.array([100, 255, 100])

mask = cv2.inRange(img, low_G, up_G)
print(mask)
print(type(mask))
masked = np.copy(img)
masked[mask != 0] = [0,0,0]
img1[mask == 0] = [0,0,0]
final = img1 + masked
cv2.imshow('c', final)
"""
 


