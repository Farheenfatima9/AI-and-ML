import cv2
import numpy as np

# Image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 07\ baby.jpg", -1)
Image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 07\Act.jpg", 0)
cv2.imshow("", Image)
cv2.waitKey()

r, c = np.shape(Image)
M = np.mean(Image)

while True:
    C1 = []
    C2 = []
    for i in range(r):
        for j in range(c):
            if Image[i, j] >= M:
                C2.append(Image[i, j])
            else:
                C1.append(Image[i, j])

    m1 = np.mean(C1)
    m2 = np.mean(C2)
    m3 = (m1 + m2) / 2

    if M == m3:
        break
    else:
        M = m3
        continue

New = np.zeros((r, c), dtype=np.uint8)
for i in range(r):
    for j in range(c):
        if Image[i, j] >= M:
            New[i, j] = 255
        else:
            New[i, j] = 0

cv2.imshow("", New)
cv2.waitKey()
