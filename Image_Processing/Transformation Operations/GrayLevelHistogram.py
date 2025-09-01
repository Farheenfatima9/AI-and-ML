import numpy as np
import cv2
import matplotlib.pyplot as plt

# Read image in grayscale
image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 04\kkk.png", 0)
cv2.imshow("Original Image", image)
cv2.waitKey()

# Initialize histogram array (256 bins for gray levels)
hist = np.zeros(256, dtype=int)

# Count pixel intensities
r, c = np.shape(image)
for i in range(r):
    for j in range(c):
        label = image[i, j]
        hist[label] += 1

# Plot histogram
plt.bar(range(256), hist, color='gray')
plt.xlim([0, 255])
plt.title('Histogram')
plt.xlabel('Gray Level')
plt.ylabel('Frequency')
plt.show()
