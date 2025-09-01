import numpy as npy

def block_sum(arr):
    sumarr = npy.zeros((3, 3), dtype=int)
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            sumarr[x // 3][y // 3] = npy.sum(arr[x:x+3, y:y+3])
    return sumarr

Array = npy.random.randint(1, 10, size=(9, 9))
print("Original Array of Order 9X9: ")
print(Array)

SUM = block_sum(Array)
print("Sum of 3X3 Matrix: ")
print(SUM)
