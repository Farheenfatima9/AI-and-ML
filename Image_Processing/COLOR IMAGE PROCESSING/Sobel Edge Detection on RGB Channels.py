import numpy as np
import cv2

# Read image
image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 10\Picture.tif")
cv2.imshow("Original Image", image)

# Split channels
b, g, r = cv2.split(image)

def sobel_channel(channel):
    Gx = cv2.Sobel(channel, cv2.CV_64F, 1, 0, ksize=3)
    Gy = cv2.Sobel(channel, cv2.CV_64F, 0, 1, ksize=3)
    G = np.sqrt(Gx**2 + Gy**2)        # gradient magnitude
    G = cv2.convertScaleAbs(G)        # convert to 0-255
    return G

# Apply Sobel to each channel
Gb = sobel_channel(b)
Gg = sobel_channel(g)
Gr = sobel_channel(r)

# Merge channels back
sobel_image = cv2.merge([Gb, Gg, Gr])

# Show results
cv2.imshow("Blue Channel Edges", Gb)
cv2.imshow("Green Channel Edges", Gg)
cv2.imshow("Red Channel Edges", Gr)
cv2.imshow("Sobel Edge Image", sobel_image)

cv2.waitKey()
cv2.destroyAllWindows()
