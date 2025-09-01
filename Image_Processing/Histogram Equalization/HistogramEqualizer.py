import matplotlib.pyplot as plt
import numpy as np
import cv2

def calculate_histogram_equalization(image):
    size = np.shape(image)
    histr = cv2.calcHist([image], [0], None, [256], [0, 256])
    c = size[0] * size[1]
    
    # Probability Density Function (PDF)
    PDF = histr / c
    
    # Cumulative Distribution Function (CDF)
    CDF = PDF.copy()
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

# Load image (grayscale)
mat = cv2.imread(r"D:\Semester 6\DIP\Labs\Lab 05\Capture.jpg", 0)
cv2.imshow("Original Image", mat)
cv2.waitKey()

# Plot original histogram
histr = cv2.calcHist([mat], [0], None, [256], [0, 256])
plt.plot(histr, label="Original Histogram")
plt.legend()
plt.show()

# User choice
i = int(input("Enter 1 for Global and 2 for Local: "))

if i == 1:
    # Global Histogram Equalization
    new = calculate_histogram_equalization(mat)

elif i == 2:
    # Local Histogram Equalization (divide into 3x3 blocks)
    rows, cols = mat.shape
    block_rows = rows // 3
    block_cols = cols // 3
    new = np.zeros_like(mat)

    for r in range(3):
        for c in range(3):
            row_start, row_end = r * block_rows, (r + 1) * block_rows
            col_start, col_end = c * block_cols, (c + 1) * block_cols
            
            block = mat[row_start:row_end, col_start:col_end]
            new_block = calculate_histogram_equalization(block)
            new[row_start:row_end, col_start:col_end] = new_block

else:
    print("No operation for this number.")
    new = mat

cv2.imshow("Equalized Image", new)
cv2.waitKey()

# Plot equalized histogram
newhistr = cv2.calcHist([new], [0], None, [256], [0, 256])
plt.plot(newhistr, label="Equalized Histogram", color='red')
plt.legend()
plt.show()
