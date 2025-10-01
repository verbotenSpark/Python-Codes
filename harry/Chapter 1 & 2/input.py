
# string input

    # a is taken input as string
# a = input("enter first number: ")   
    # same for b
# b = input("enter second number: ")  

    # printing separately we dont have issues
# print("a = ",a)      
# print("b = ",b)

    # but on  performing sum, since the input is string the numbers concatenate
# print ("sum = ",a+b)
    # to avoid this cast the input as:   a = int(input("Enter First Number: "))

# integer input
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("a = ",a)      
print("b = ",b)

print ("sum = ",a+b)
