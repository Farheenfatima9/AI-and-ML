import numpy as np
import cv2

def creatingmask():
    x = int(input("Enter the mask size: "))
    if x % 2 == 0:
        print("Not right mask size. Must be odd.")
        return None
    else:
        mask = np.ones((x, x), dtype=np.uint8)  # not used in max filter, but created
        return mask

def Padding(image, paddingsize):
    # Pad image with zeros on all sides
    return np.pad(image, ((paddingsize, paddingsize), (paddingsize, paddingsize)), mode='constant')

def Filter(img, fil):
    a = fil.shape[0] // 2
    size = img.shape
    r = size[0] - 2 * a
    c = size[1] - 2 * a

    beau = np.zeros((r, c), dtype=np.uint8)

    for i in range(a, size[0] - a):
        for j in range(a, size[1] - a):
            alpha = img[i - a:i + a + 1, j - a:j + a + 1]
            z = np.max(alpha)  # maximum pixel in region
            beau[i - a, j - a] = z

    cv2.imshow("Max Filtered Image", beau)
    cv2.waitKey()
    return beau


# Main
mask = creatingmask()
if mask is not None:
    image = cv2.imread(r"D:\Semester 6\DIP\Labs\Lab 06\Seed.tif", 0)
    cv2.imshow("Original Image", image)
    cv2.waitKey()

    padding_size = mask.shape[0] // 2
    newimage = Padding(image, padding_size)

    Filter(newimage, mask)
