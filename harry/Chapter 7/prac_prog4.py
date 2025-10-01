no = int(input("Enter a Number: "))

for i in range(2,int(no/2)):
    if(no%i == 0):
        print(f"Not a prime Number, divisible by {i}")
        break
       