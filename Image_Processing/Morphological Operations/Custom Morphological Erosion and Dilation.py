import numpy as np
import cv2

def Erosion(image, mask):
    r, c = np.shape(image)
    mrows, mcols = np.shape(mask)
    PaddedImage = np.pad(image, ((mrows//2, mrows//2), (mcols//2, mcols//2)), mode='constant')
    Newimage = np.zeros((r, c), dtype=np.uint8)

    for i in range(r):
        for j in range(c):
            a = PaddedImage[i:i+mrows, j:j+mcols]
            if np.all(a == mask):   # erosion → all pixels must match mask
                Newimage[i, j] = 255
    return Newimage

def Dilation(image, mask):
    r, c = np.shape(image)
    mrows, mcols = np.shape(mask)
    PaddedImage = np.pad(image, ((mrows//2, mrows//2), (mcols//2, mcols//2)), mode='constant')
    Newimage = np.zeros((r, c), dtype=np.uint8)

    for i in range(r):
        for j in range(c):
            a = PaddedImage[i:i+mrows, j:j+mcols]
            if np.any(a == mask):   # dilation → at least one overlap
                Newimage[i, j] = 255
    return Newimage

image = cv2.imread(r"D:\Semester 6\DIP\Labs\Lab 09\Fingerprint.tif", 0)

Mask = np.ones((3, 3), dtype=np.uint8) * 255  # structuring element

Eroded_Image = Erosion(image, Mask)
Dilated_Image = Dilation(Eroded_Image, Mask)

cv2.imshow("Original Image", image)
cv2.imshow("Erosion", Eroded_Image)
cv2.imshow("Dilation", Dilated_Image)
cv2.waitKey()
cv2.destroyAllWindows()
