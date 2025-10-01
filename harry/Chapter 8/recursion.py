
def fact(no):
    if(no == 1 or no == 0):
        return 1
    return no*fact(no-1)

no = int(input("Enter a number: "))
print(fact(no))