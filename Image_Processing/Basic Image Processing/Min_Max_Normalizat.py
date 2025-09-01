# Minimum Value
def min(mylist):
    minval = mylist[0]
    for value in mylist:
        if value < minval:
            minval = value
    return minval

# Maximum Value
def max(mylist):
    maxval = mylist[0]
    for value in mylist:
        if value > maxval:
            maxval = value
    return maxval

def MinMaxNormalization(lst, minimumvalue, maximumvalue):
    normalized_lst = [(x - minimumvalue) / (maximumvalue - minimumvalue) for x in lst]
    return normalized_lst

mylist = [5, 7, 10, 14, 25]
minimum = min(mylist)
maximum = max(mylist)
normallist = MinMaxNormalization(mylist, minimum, maximum)

print("Min_Max_Normalization: ", normallist)
