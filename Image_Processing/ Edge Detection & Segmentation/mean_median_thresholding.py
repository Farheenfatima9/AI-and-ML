import cv2
import numpy as np

Image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 07\input.png", 0)
cv2.imshow("", Image)
cv2.waitKey()

r, c = np.shape(Image)
Mean_Threhold = np.zeros((r, c), dtype=np.uint8)
Medn_Threhold = np.zeros((r, c), dtype=np.uint8)

Mean = np.mean(Image)
Median = np.median(Image)

for i in range(r):
    for j in range(c):
        if Image[i, j] >= Mean:
            Mean_Threhold[i, j] = 255
        else:
            Mean_Threhold[i, j] = 0

for i in range(r):
    for j in range(c):
        if Image[i, j] >= Median:
            Medn_Threhold[i, j] = 255
        else:
            Medn_Threhold[i, j] = 0

cv2.imshow("Mean", Mean_Threhold)
cv2.waitKey()
cv2.imshow("Median", Medn_Threhold)
cv2.waitKey()
