name = input("Enter Your Name: ")

# Method 1
nameList = ["hello","world","rohan","willy"]
if(name == nameList[0] or name == nameList[1] or name == nameList[2] or name == nameList[3]):
    print("Name is present")
else:
    print("Name is not present")
# print(name.find(nameList[0]))

# Method 2
if(name in nameList):
    print("Name is present")
else:
    print("Name is not present")
