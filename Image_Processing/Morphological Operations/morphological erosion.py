import numpy as np
import cv2

def Erosion(image, mask):
    r, c = image.shape
    mrows, mcols = mask.shape
    
    # Pad the image
    PaddedImage = np.pad(image, 
                         ((mrows//2, mrows//2), (mcols//2, mcols//2)), 
                         mode='constant', constant_values=0)
    
    Newimage = np.zeros((r, c), dtype=np.uint8)
    
    for i in range(r):
        for j in range(c):
            a = PaddedImage[i:i+mrows, j:j+mcols]
            # Erosion condition: all mask pixels fit inside the object
            if np.all(a[mask == 255] == 255):
                Newimage[i, j] = 255
    
    return Newimage

# Load grayscale
image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 09\kk.png", 0)

# Convert to binary (important for erosion)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Structuring element
Mask = np.ones((18, 18), dtype=np.uint8) * 255

# Apply erosion
Eroid_Image = Erosion(binary, Mask)

# Show results
cv2.imshow("Original", image)
cv2.imshow("Binary", binary)
cv2.imshow("Erosion", Eroid_Image)

# Count connected components
count, labels = cv2.connectedComponents(Eroid_Image)
print("Total Number of objects are:", count - 1)  # subtract background

cv2.waitKey(0)
cv2.destroyAllWindows()
