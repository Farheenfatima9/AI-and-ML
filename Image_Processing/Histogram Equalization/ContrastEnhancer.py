import numpy as np
import cv2

def global_equalization(image):
    size = np.shape(image)
    histr = cv2.calcHist([image], [0], None, [256], [0, 256])
    c = size[0] * size[1]

    # Probability Density Function (PDF)
    PDF = histr / c
    CDF = PDF.copy()

    # Cumulative Distribution Function (CDF)
    for i in range(1, len(CDF)):
        CDF[i] = CDF[i] + CDF[i - 1]

    # Transformation function
    trans = np.round(CDF * 255)

    # Apply transformation
    newimage = np.zeros(size, dtype=np.uint8)
    for i in range(size[0]):
        for j in range(size[1]):
            p = image[i, j]
            newimage[i, j] = trans[p]

    return newimage


def local_enhancement(image, mg, sd):
    ms = np.mean(image)
    d = np.std(image)

    # Constants for local enhancement
    k0 = 0
    k1 = 0.25
    k2 = 0
    k3 = 0.1

    if (k0 * mg) <= ms <= (k1 * mg) and (k2 * sd) <= d <= (k3 * sd):
        image = image * 22.8
        image = np.clip(image, 0, 255)  # avoid overflow

    return image.astype(np.uint8)


# Load image in grayscale
mat = cv2.imread(r"D:\Semester 6\DIP\Labs\Lab 05\Capture2.jpg", 0)
cv2.imshow("Original Image", mat)
cv2.waitKey()

# Ask user
choice = int(input("Enter 1 for Global and 2 for Local: "))

if choice == 1:
    new = global_equalization(mat)

elif choice == 2:
    sd = np.std(mat)
    me = np.mean(mat)
    rows, cols = mat.shape
    new = np.zeros((rows, cols), dtype=np.uint8)

    block_rows = rows // 3
    block_cols = cols // 3

    for r in range(3):
        for c in range(3):
            row_start, row_end = r * block_rows, (r + 1) * block_rows
            col_start, col_end = c * block_cols, (c + 1) * block_cols

            block = mat[row_start:row_end, col_start:col_end]
            new_block = local_enhancement(block, me, sd)
            new[row_start:row_end, col_start:col_end] = new_block
else:
    new = mat
    print("Invalid input, showing original image.")

cv2.imshow("Enhanced Image", new)
cv2.waitKey()
