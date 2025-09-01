import numpy as np
import cv2

# Read image in grayscale
image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 04\kkk.png", 0)
cv2.imshow("Original Image", image)
cv2.waitKey()

r, c = np.shape(image)

# Calculate mean
meanvalue = image.mean()

# Create empty images
image1 = np.zeros([r, c], dtype=np.uint8)
image2 = np.zeros([r, c], dtype=np.uint8)
image3 = np.zeros([r, c], dtype=np.uint8)

for i in range(r):
    for j in range(c):
        if image[i, j] < meanvalue:
            image1[i, j] = 0
            image2[i, j] = 255
        else:
            image1[i, j] = 255
            image2[i, j] = 0

        # For image3: mean thresholding with ±20 tolerance
        if meanvalue - 20 <= image[i, j] <= meanvalue + 20:
            image3[i, j] = 0
        else:
            image3[i, j] = 255

cv2.imshow("Image1", image1)
cv2.waitKey()

cv2.imshow("Image2", image2)
cv2.waitKey()

cv2.imshow("Image3", image3)
cv2.waitKey()
