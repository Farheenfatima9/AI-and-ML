import numpy as np
import cv2 as cv

def Erosion(img, mask):
    rows, cols = np.shape(mask)
    padding_size = rows // 2
    padded_img = np.pad(img, (padding_size, padding_size), 'constant')
    r, c = np.shape(padded_img)
    Eroded_Img = np.zeros((r, c), dtype=np.uint8)
    i_end = r - padding_size
    j_end = c - padding_size

    for i in range(padding_size, i_end):
        for j in range(padding_size, j_end):
            Temp = padded_img[i - padding_size:i + padding_size + 1,
                              j - padding_size:j + padding_size + 1]  # under structuring element
            Result = Temp * mask
            Eroded_Img[i, j] = np.min(Result)
    return Eroded_Img


def Dilation(img, mask):
    rows, cols = np.shape(mask)
    padding_size = rows // 2
    padded_img = np.pad(img, (padding_size, padding_size), 'constant')
    r, c = np.shape(padded_img)
    Dilated_Img = np.zeros((r, c), dtype=np.uint8)
    i_end = r - padding_size
    j_end = c - padding_size

    for i in range(padding_size, i_end):
        for j in range(padding_size, j_end):
            Temp = padded_img[i - padding_size:i + padding_size + 1,
                              j - padding_size:j + padding_size + 1]
            Result = Temp * mask
            Dilated_Img[i, j] = np.max(Result)
    return Dilated_Img


# ---------------- Main ----------------
img = cv.imread("D:\Semester 6\DIP\Labs\Lab 09\ctscan.tif", 0)
Mask = np.ones((3, 3), dtype=np.uint8)

Dilated_img = Dilation(img, Mask)
Eroded_Img = Erosion(img, Mask)
Gradient_img = Dilated_img - Eroded_Img

cv.imshow('Original Image', img)
cv.imshow('Eroded Image', Eroded_Img)
cv.imshow('Dilated Image', Dilated_img)
cv.imshow('Morphological Gradient Image', Gradient_img)
cv.waitKey()
