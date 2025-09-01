import numpy as np
import cv2

myimage=cv2.imread("D:\Semester 6\DIP\Labs\Lab 02\Flip.jpg", -1)
cv2.imshow("Image ", myimage)
cv2.waitKey()

size=np.shape(myimage)
print(size)

newimage=np.ones(size,dtype=np.uint8)
r=size[0]//2
c=size[1]
print(r,c)

for i in range(r):
    for j in range(c):
        newimage[i,j]=myimage[i,j]
        m=i
        n=j
m=m+1

for i in reversed(range(r)):
     n = 0
     for j in range(c):
        newimage[m,n]=myimage[i,j]
        n=n+1
     m=m+1
     
cv2.imshow("CenterModifying", newimage)
cv2.waitKey()
cv2.imwrite("CenterModifying.jpg", newimage)