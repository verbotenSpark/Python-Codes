print("Enter 4 Numbers")
a = int(input(""))
b = int(input(""))
c = int(input(""))
d = int(input(""))
if(a>b and a>c and a>d):
    print(f"{a} is the greatest number")
elif(b>c and b>d):
    print(f"{b} is the greatest number")
elif(c>d):
    print(f"{c} is the greatest number")
else:
    print(f"{d} is the greatest number")


