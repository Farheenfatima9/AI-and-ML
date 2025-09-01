import numpy as np
import cv2

def ChessBoardDistance(zer):
    r, c = np.shape(zer)
    m = r // 2
    n = c // 2
    # print(m, n)
    newimage = np.zeros((r, c), dtype=np.uint8)
    for i in range(r):
        for j in range(c):
            a = abs(i - m)
            b = abs(j - n)
            # print(i, j)
            # print(":::", a, b)
            z = max(a,b)
            # print("z: ", z)
            newimage[i, j] = z
    cv2.imshow("Image: ", newimage)
    cv2.waitKey()

def CityBlockDistance(zer):
     r, c = np.shape(zer)
     m = r // 2
     n = c // 2
     # print(m, n)
     newimage = np.zeros((r, c), dtype=np.uint8)
     for i in range(r):
        for j in range(c):
            a = i - m
            b = j - n
            # print(i, j)
            # print(":::", a, b)
            z = abs(a)+abs(b)
            # print("z: ", z)
            newimage[i, j] = z
     cv2.imshow("Image: ", newimage)
     cv2.waitKey()
def EuclidianDistance(zer):
    r, c=np.shape(zer)
    m=r//2
    n=c//2
    # print(m,n)
    newimage=np.zeros((r,c), dtype=np.uint8)
    for i in range(r):
        for j in range(c):
            a=i-m
            b=j-n
            # print(i,j)
            # print(":::",a,b)
            z=np.sqrt(np.square(a)+np.square(b))
            # print("z: ",z)
            newimage[i,j]=z
    cv2.imshow("Image: ", newimage)
    cv2.waitKey()


zer=np.zeros((501,501),dtype=np.uint8)

print("Select any one to calculate distance\n 1: Euclidian Distance\n 2:City Block Distance\n 3: ChessBoardDistance")
x=input()
if int(x)==1:
    EuclidianDistance(zer)
elif int(x)==2:
    CityBlockDistance(zer)
elif int(x)==3:
    ChessBoardDistance(zer)
else:
    print("Invalid Input. No, operation for this number.")