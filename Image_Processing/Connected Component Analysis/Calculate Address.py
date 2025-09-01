import numpy as np

def CalculateDistance(p1, p2, n):
    if n == 1:
        a = p1[0] - p2[0]
        b = p1[1] - p2[1]
        z = np.sqrt(np.square(a) + np.square(b))
        print("Euclidian Distance is: ", z)

    elif n == 2:
        a = p1[0] - p2[0]
        b = p1[1] - p2[1]
        z = abs(a) + abs(b)
        print("City Block Distance is: ", z)

    elif n == 3:
        a = abs(p1[0] - p2[0])
        b = abs(p1[1] - p2[1])
        z = max(a, b)
        print("Chess Board Distance is: ", z)

    else:
        print("Invalid Input. No operation for this number.")


x1 = int(input("Enter i of first point: "))
y1 = int(input("Enter j of first point: "))
x2 = int(input("Enter i of second point: "))
y2 = int(input("Enter j of second point: "))

p = [x1, y1]
q = [x2, y2]

print("Select any one to calculate distance\n 1: Euclidian Distance\n 2: City Block Distance\n 3: Chess Board Distance")
x = int(input())

CalculateDistance(p, q, x)
