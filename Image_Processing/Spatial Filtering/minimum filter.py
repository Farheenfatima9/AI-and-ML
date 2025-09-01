import numpy as np
import cv2

def creating_mask():
    x = int(input("Enter the mask size: "))
    if x % 2 == 0:
        print("Not a valid mask size. Must be odd.")
        return None
    else:
        mask = np.ones((x, x), dtype=np.uint8)   # mask (not really used for min filter)
        return mask

def padding(image, padding_size):
    # Pad equally on all sides
    return np.pad(image, ((padding_size, padding_size), (padding_size, padding_size)), mode='constant')

def min_filter(img, fil):
    a = fil.shape[0] // 2   # half mask size
    rows, cols = img.shape
    r = rows - 2 * a
    c = cols - 2 * a

    output = np.zeros((r, c), dtype=np.uint8)

    for i in range(a, rows - a):
        for j in range(a, cols - a):
            region = img[i - a:i + a + 1, j - a:j + a + 1]
            z = np.min(region)  # take minimum pixel value
            output[i - a, j - a] = z

    cv2.imshow("Min Filtered Image", output)
    cv2.waitKey()
    return output


# Main code
mask = creating_mask()
if mask is not None:
    image = cv2.imread(r"D:\Semester 6\DIP\Labs\Lab 06\Seed.tif", 0)
    cv2.imshow("Original Image", image)
    cv2.waitKey()

    padding_size = mask.shape[0] // 2
    new_image = padding(image, padding_size)

    min_filter(new_image, mask)
