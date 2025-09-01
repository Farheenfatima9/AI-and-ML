import numpy as np
import cv2

# Read image in grayscale
image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 04\kkk.png", 0)
cv2.imshow("Original Image", image)
cv2.waitKey()

# Gamma values
γ = [0.2, 0.5, 1.2, 1.8]

a = np.shape(γ)
print(a)

for i in range(a[0]):
    p = np.power((image / 255), γ[i])
    s = 255 * p
    arr = np.array(s, np.uint8)
    cv2.imshow(f"Gamma {γ[i]}", arr)
    cv2.waitKey()
