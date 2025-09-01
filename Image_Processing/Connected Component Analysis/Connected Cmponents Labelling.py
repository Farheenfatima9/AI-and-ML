import numpy as np
import cv2

array = cv2.imread("D:\Semester 6\DIP\Labs\Lab 03\BlackWhiteBoxes.jpg", 0)
cv2.imshow("Image ", array)
cv2.waitKey()

size = np.shape(array)
av = np.average(array)

for i in range(size[0]):
    for j in range(size[1]):
        if array[i, j] > av:
            array[i, j] = 1
        else:
            array[i, j] = 0

label = np.zeros((size[0], size[1]), dtype=np.uint8)
la = 0

for i in range(size[0]):
    for j in range(size[1]):
        if i == 0:
            if j == 0:
                if array[i, j] == 1:
                    la = la + 1
                    label[i, j] = la
                else:
                    label[i, j] = 0
            else:
                if array[i, j] == 1:
                    if array[i, j-1] == 1:
                        label[i, j] = label[i, j-1]
                    else:
                        la = la + 1
                        label[i, j] = la
                else:
                    label[i, j] = 0
        else:
            if j == 0:
                if array[i, j] == 1:
                    if array[i-1, j] == 0:
                        la = la + 1
                        label[i, j] = la
                    else:
                        label[i, j] = label[i-1, j]
                else:
                    label[i, j] = 0
            else:
                if array[i, j] == 1:
                    if array[i-1, j] == 1 and array[i, j-1] == 1:
                        if label[i-1, j] == label[i, j-1]:
                            label[i, j] = label[i-1, j]
                        else:
                            label[i, j] = min(label[i-1, j], label[i, j-1])
                    elif array[i-1, j] == 0 and array[i, j-1] == 0:
                        la = la + 1
                        label[i, j] = la
                    else:
                        if array[i-1, j] == 0:
                            label[i, j] = label[i, j-1]
                        else:
                            label[i, j] = label[i-1, j]
                else:
                    label[i, j] = 0

print("Labels: ", la)

for i in range(size[0]):
    for j in range(size[1]):
        if i == 0 and j == 0:
            continue
        elif label[i, j] != 0:
            if label[i, j-1] != 0:
                minimumvalue = min(label[i, j], label[i, j-1])
                maximumvalue = max(label[i, j], label[i, j-1])
                for k in range(size[0]):
                    for m in range(size[1]):
                        if label[k, m] == maximumvalue:
                            label[k, m] = minimumvalue

for i in range(size[0]):
    for j in range(size[1]):
        if i == 0:
            continue
        elif label[i, j] != 0:
            if label[i-1, j] != 0:
                minimumvalue = min(label[i, j], label[i-1, j])
                maximumvalue = max(label[i, j], label[i-1, j])
                for k in range(size[0]):
                    for m in range(size[1]):
                        if label[k, m] == maximumvalue:
                            label[k, m] = minimumvalue

total = 0
for i in range(size[0]):
    for j in range(size[1]):
        if i == 0 and j == 0:
            if label[i, j] == 0:
                a = 0
            else:
                a = label[i, j]
            total = total + 1
        else:
            if label[i, j] > a:
                a = label[i, j]
                total = total + 1

print("Total Objects: ", total)
