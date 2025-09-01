import cv2
import numpy as np

Image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 07\input2.png", 0)
cv2.imshow("", Image)
cv2.waitKey()

Gx = cv2.Sobel(Image, cv2.CV_64F, 1, 0, ksize=3)
Gy = cv2.Sobel(Image, cv2.CV_64F, 0, 1, ksize=3)
G = np.sqrt(np.square(Gx) + np.square(Gy))

r, c = np.shape(G)
mag = np.zeros((r, c), dtype=np.uint8)
phase = np.zeros((r, c), dtype=np.uint8)
both = np.zeros((r, c), dtype=np.uint8)

angle = np.arctan(Gy, Gx)
angle = np.degrees(angle)

Maxg = np.max(G)
Maxg = Maxg * 0.7

for i in range(np.shape(G)[0]):
    for j in range(np.shape(G)[1]):
        if G[i, j] >= Maxg:
            mag[i, j] = G[i, j]

for i in range(angle.shape[0]):
    for j in range(angle.shape[1]):
        if angle[i, j] == 45 and angle[i, j] == 90:
            phase[i, j] = angle[i, j]

cv2.imshow("Magnitude are in top 30%", G)
cv2.waitKey()

cv2.imshow("Angle equals to 45 and 90", angle)
cv2.waitKey()

for i in range(np.shape(G)[0]):
    for j in range(np.shape(G)[1]):
        if G[i, j] <= Maxg and angle[i, j] == 45 and angle[i, j] == 90:
            G[i, j] = angle[i, j]

cv2.imshow("Both", G)
cv2.waitKey()
