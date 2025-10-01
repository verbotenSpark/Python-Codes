
# File Methods

# read all lines and return as list Method
def readList():
    # below line opens said file as: open("File_Name","r"), r is read mode
    f = open("file.txt") 
    c = f.readlines()    # reads all lines in file, as a list
    print(c)
    f.close()            # closes file

# read file Method
def read():
    f = open("file.txt")
    c = f.read()         # returns file txt as it is
    print(c)
    f.close()

# read file by line Method
def readLine():
    f = open("file.txt")
    c = f.readline()     # reads one line of the file
    print(c)
    f.close()

# append Method
def append():
    f = open("file.txt","a") # opens file in append mode
    f.write("Fourth line\n")
    f.close

# write Method
def write():
    f = open("file.txt","w") # opens file in write mode
    f.write("What line")  # replaces all content in file with the given string
    f.close

readList()
append()
read()

# Recommended Method to open files

'''
Syntax for With Method:

with open("File_Name.txt") as VarName:
    # code..
# Automatically file is closed
'''
with open("file.txt") as f:
    f.read()