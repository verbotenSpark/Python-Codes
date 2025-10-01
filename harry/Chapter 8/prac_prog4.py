def sumN(no):
    if(no == 1):
        return 1
    return  no + sumN(no-1)


no = int(input("Enter a Number: "))
print(sumN(no))