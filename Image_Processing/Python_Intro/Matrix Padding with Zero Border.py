import numpy as np
import cv2

def imagecreation(s, p):
    my_array=np.ones((s+2*p, s+2*p), dtype=np.uint8)
    my_array=my_array*255
    a=len(my_array)
    my_array[0:2*p, :] = 0
    my_array[a-(2*p):a, :] = 0
    my_array[:, 0:2*p] = 0
    my_array[:, a-(2*p):a] = 0
    cv2.imshow("White: ", my_array)
    cv2.waitKey()
x=int(input("Enter size of image: "))
y=int(input("Enter Padding: "))
imagecreation(x, y)