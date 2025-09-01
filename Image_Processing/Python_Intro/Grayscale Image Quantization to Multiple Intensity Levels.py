import numpy as np
import cv2
def IntensityResolution(N, size):
 image=cv2.imread('D:\Semester 6\DIP\Labs\Lab 02\Graylevelimage.jpg',0)
 new_image=cv2.resize(image, (size,size))
 r, c=np.shape(new_image)
 division=int(256/N)
 for i in range(r):
   for j in range(c):
      levels=int((new_image[i,j])/division)
      new_image[i,j]=levels*division
 return new_image

x = int(input('Enter size of image: '))
newimage1 = IntensityResolution(16, x)

cv2.imshow('New image 16', newimage1)
cv2.waitKey()

newimage2 = IntensityResolution(4, x)
cv2.imshow('New image 4', newimage2)
cv2.waitKey()

newimage3 = IntensityResolution(2, x)
cv2.imshow('New image 1', newimage3)
cv2.waitKey()