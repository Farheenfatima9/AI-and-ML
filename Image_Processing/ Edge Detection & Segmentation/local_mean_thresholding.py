import cv2
import numpy as np

def locally(image):
    size = np.shape(image)
    newimage = np.zeros((size), dtype=np.uint8)
    Mean = np.mean(image)
    for i in range(size[0]):
        for j in range(size[1]):
            if image[i, j] >= Mean:
                newimage[i, j] = 255
            else:
                newimage[i, j] = 0
    return newimage


Image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 07\input.png", 0)
cv2.imshow("", Image)
cv2.waitKey()

x = np.shape(Image)
new = np.zeros((x), dtype=np.uint8)

r = int(np.round(x[0] / 3))
c = int(np.round(x[1] / 3))

a = 0
b = 3
for i in range(r):
    e = 0
    f = 3
    for j in range(c):
        z = Image[a:b, e:f]
        r = locally(z)
        new[a:b, e:f] = r
        e = e + 3
        f = f + 3
    a = a + 3
    b = b + 3

cv2.imshow("New", new)
cv2.waitKey()
