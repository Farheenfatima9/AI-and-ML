import numpy as np
import cv2

myimage=cv2.imread("D:\Semester 6\DIP\Labs\Lab 02\Flip.jpg", -1)
cv2.imshow("Image ", myimage)
cv2.waitKey()
# Flip Vertical
size=np.shape(myimage)
newimage=np.ones(size,dtype=np.uint8)
row=size[0]
col=size[1]
m=row-1
n=0
print(m,n)

for i in range(row):
    n=0
    for j in range(col):
        newimage[m,n]=myimage[i,j]
        n = n +1
    m = m -1
cv2.imshow("Flip Vertical ", newimage)
cv2.waitKey()

# Flip Horizontal
row=size[0]
col=size[1]
m=0
n=col-1
for i in range(row):
    n=col-1
    for j in range(col):
        newimage[m,n]=myimage[i,j]
        n = n -1
    m = m +1
cv2.imshow("Flip Horizontal ", newimage)
cv2.waitKey()
# Flip Horizontal Vertical
row=size[0]
col=size[1]
m=row-1
n=col-1
for i in range(row):
     n=col-1
     for j in range(col):
        newimage[m,n]=myimage[i,j]
        n = n -1
     m = m -1
cv2.imshow("Flip Vertical Horizontal", newimage)
cv2.waitKey()