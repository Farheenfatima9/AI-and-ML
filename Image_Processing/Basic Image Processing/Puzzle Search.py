row = 4
col = 4

def Finding(array, inp, indx1, indx2, nrow, ncol, level):
    l = len(inp)
    if (level == l):
        return True
    if (indx1 < 0 or indx2 < 0 or indx1 >= nrow or indx2 >= ncol):
        return False
    if (array[indx1][indx2] == inp[level]):
        temp = array[indx1][indx2]
        array[indx1].replace(array[indx1][indx2], "#")

        res = (Finding(array, inp, indx1 - 1, indx2, nrow, ncol, level + 1) |
               Finding(array, inp, indx1 + 1, indx2, nrow, ncol, level + 1) |
               Finding(array, inp, indx1, indx2 - 1, nrow, ncol, level + 1) |
               Finding(array, inp, indx1, indx2 + 1, nrow, ncol, level + 1))

        array[indx1].replace(array[indx1][indx2], temp)
        return res
    else:
        return False


def CheckingMtachwords(array, inp, r, c):
    i = len(inp)
    if (i > r * c):
        return False

    for y in range(r):
        for z in range(c):
            if (array[y][z] == inp[0]):
                if (Finding(array, inp, y, z, r, c, 0)):
                    return True
    return False


grid = ["axmy", "cats", "xeet", "raks"]

print("Enter any String: ")
x = input()

if (CheckingMtachwords(grid, x, row, col)):
    print("Yes")
else:
    print("No")
