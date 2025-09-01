import numpy as np
import cv2

def Erosion(image, mask):
    r = np.shape(mask)[0] // 2
    rows, cols = np.shape(image)
    Eroded_image = np.zeros_like(image)
    padded_image = np.pad(image, (r, r))

    for i in range(r, rows + r):
        for j in range(r, cols + r):
            Eroded_image[i - r, j - r] = np.min(padded_image[i - r:i + r + 1,
                                                            j - r:j + r + 1])
    return Eroded_image


def Dilation(image, mask):
    r = np.shape(mask)[0] // 2
    rows, cols = np.shape(image)
    Dilated_image = np.zeros_like(image)
    padded_image = np.pad(image, (r, r))

    for i in range(r, rows + r):
        for j in range(r, cols + r):
            Dilated_image[i - r, j - r] = np.max(padded_image[i - r:i + r + 1,
                                                              j - r:j + r + 1])
    return Dilated_image


# ---------------- Main ----------------
image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 09\Rice.tif", 0)
Mask = np.ones([60, 60], dtype=np.uint8)

Eroded_Image = Erosion(image, Mask)
Dilated_Image = Dilation(Eroded_Image, Mask)

Top_hat = image - Dilated_Image
_, thresh = cv2.threshold(Top_hat, 60, 255, cv2.THRESH_BINARY)

cv2.imshow('Input Image', image)
cv2.imshow('Top Hat Image', thresh)
cv2.waitKey()
