import numpy as np
import cv2

# Read image in grayscale
image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 04\kkk.png", 0)
cv2.imshow("Original Image", image)
cv2.waitKey()

# Negative Image
l = 255
n = (l - 1) - image
cv2.imshow("Negative Image", n)
cv2.waitKey()

# Logarithmic Image
a = np.max(image)
c = 255 / np.log(1 + a)
L = c * (np.log(image + 1))
arr = np.array(L, np.uint8)
cv2.imshow("Logarithmic Image", arr)
cv2.waitKey()
