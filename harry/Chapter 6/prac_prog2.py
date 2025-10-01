print("Enter mark of three subjects:  ")
s1 = int(input(""))
s2 = int(input(""))
s3 = int(input(""))
max = int(input("Enter max marks: "))
s1p = (s1/max)*100
s2p = (s2/max)*100
s3p = (s3/max)*100
avg = (s1p + s2p + s3p)/3

if(s1p < 33 or s2p < 33 or s3p < 33):
    print("Student has failed in at least one subject")
elif(avg < 40):
    print("Student has passed in all subjects but agrregately failed")
else:
    print("Student has passed :P")