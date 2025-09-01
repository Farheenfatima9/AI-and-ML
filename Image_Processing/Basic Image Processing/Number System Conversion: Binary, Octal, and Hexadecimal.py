def DecToOther(d, n):
    b = 0
    m = 1
    i=0
    mylist=[]
    if n==16:
        while d > 0:
            r=d%n
            if r>=10:
                r=r+55
            else:
                r=r+48
            r=chr(r)
            mylist.insert(i, r)
            i=i+1
            d=int(d/n)
        return mylist
    else:
        while d > 0:
            b=d%n
            mylist.insert(i,b)
            i=i+1
            m = m * 10
            d = int(d / n)
        return mylist
while("true"):
    print("Enter a number to convert it into different number system: ")
    x = input()
    if x.isdigit():
        print(" 1: Binary\n 2: Octal\n 3: Hexadecimal")
        y = input()
        if (int(y) == 1):
            print("Binary: ", end='')
            x=int(x)
            a = DecToOther(x, 2)
            z = len(a)
            z = z - 1
            while z >= 0:
                print(a[z], end='')
                z = z - 1
        elif (int(y) == 2):
            print("Octal: ", end='')
            x = int(x)
            a = DecToOther(x, 8)
            z = len(a)
            z = z - 1
            while z >= 0:
                print(a[z], end='')
                z = z - 1
        elif (int(y) == 3):
            print("Hexadecimal: ", end='')
            x = int(x)
            a = DecToOther(x, 16)
            z=len(a)
            z=z-1
            while z>=0:
                print(end=a[z])
                z=z-1
        else:
            print("Invalid Input. No, operation for this number.")
            break
    else:
        continue