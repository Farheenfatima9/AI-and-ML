def sorter(my_input_list, x, y):
    sorted_list=[]
    length = len(my_input_list)
    if (y == 'assending'):
        if (x == 'age'):
            i = 0
            while(i<length):
                j=i+1
                while(j<length):
                    if(my_input_list[i][0]>my_input_list[j][0]):
                        temp=my_input_list[i][0]
                        my_input_list[i][0]=my_input_list[j][0]
                        my_input_list[j][0]=temp
                    else:
                        None
                    j=j+1
                i=i+1
        elif (x == 'cgpa'):
            i = 0
            while (i < length):
                j = i + 1
                while (j < length):
                    if (my_input_list[i][1] > my_input_list[j][1]):
                        temp = my_input_list[i][1]
                        my_input_list[i][1] = my_input_list[j][1]
                        my_input_list[j][1] = temp
                    else:
                        None
                    j = j + 1
                i = i + 1

        sorted_list=my_input_list
    elif (y=="decending"):
        if (x == 'age'):
            i = 0
            while(i<length):
                j=i+1
                while(j<length):
                    if(my_input_list[i][0]<my_input_list[j][0]):
                        temp=my_input_list[i][0]
                        my_input_list[i][0]=my_input_list[j][0]
                        my_input_list[j][0]=temp
                    else:
                        None
                    j=j+1
                i=i+1
        elif (x == 'cgpa'):
            i = 0
            while (i < length):
                j = i + 1
                while (j < length):
                    if (my_input_list[i][1] < my_input_list[j][1]):
                        temp = my_input_list[i][1]
                        my_input_list[i][1] = my_input_list[j][1]
                        my_input_list[j][1] = temp
                    else:
                        None
                    j = j + 1
                i = i + 1
        sorted_list = my_input_list
    else:
        None
    return sorted_list


my_input_list = [[29, 3.2, 'Rawalpindi'], [22, 4.0, 'Islamabad'], [12, 0,'Karachi']]
print("Enter age or cgpa for sorting: ")
a = input()
print("Enter assending or decending for sorting: ")
b=input()
print("Initial List: ", my_input_list)
s=sorter(my_input_list, a, b)
print("Sorted List: ", s)