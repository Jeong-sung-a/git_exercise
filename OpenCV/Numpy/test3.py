import cv2
import numpy as np
img = cv2.imread("../Show1/Resource/girl2.jpg")
print(img)
print(img.shape)

a = np.empty_like(img)
b = np.zeros_like(img)
c = np.ones_like(img)
d = np.full_like(img, 255)

print(a)
print(a.shape)

print(b)
print(b.shape)

print(c)
print(c.shape)

print(d)
print(d.shape)