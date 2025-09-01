import numpy as np
import cv2

# Read image in grayscale
image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 04\kkk.png", 0)
cv2.imshow("Original Image", image)
cv2.waitKey()

# Get image dimensions
r, c = np.shape(image)

# Replace pixel values in range [100, 200] with 210
for i in range(r):
    for j in range(c):
        if 100 <= image[i, j] <= 200:
            image[i, j] = 210

# Show updated image
cv2.imshow("Modified Image", image)
cv2.waitKey()
