import numpy as np
import cv2
def colouredsidedimage(size):
    white=np.ones((size,size, 3), dtype=np.uint8)
    white=white*255
    s=len(white)
    box=s//8
    print("Box Size: ", box)
    white[0:box, 0:box] = (0,0,255)
    white[0:box,s - box:s] = (0, 255, 0)
    white[s - box:s, 0:box] = (255, 0, 0)
    white[s-box:s, s-box:s]=(0,0, 0)
    cv2.imshow("White ", white)
    cv2.waitKey()

    
x=int(input("Enter the size of image: "))
colouredsidedimage(int(x))