# different methods to store strings
a = 'single quoted'
b = "double quoted"
c = '''single triple quoted'''
d = """double triple quoted"""

print(a," ",b," ",c," ",d)

print()

# String Slicing
name = "peogammings"
nameCut = name[0:4]      #store string from index 0 till 3 (exclude 4)
print(nameCut)
nameChar = name[2]   #store charat index 2 of name in nameChar
print(nameChar) 

# negative Slicing
name = "Penglings"
nameNegative = name[-6:-1]      
    # -ve numbering start from right and goes to left,here the last s is -1 & P is -9
print(nameNegative)

# empty colon spaces
name = "penwings"
startMt = name[:6]  # the starting index is considered 0
endMt = name[2:]   # the ending index is considered as the string length

#Slicing with Skip
name = "0123456789"
skipSlice = name[0:8:2]
# 01234567 is sliced then 0 is stored then next 1 nos are skipped and 2 is stored then repeat abd store 4 then skip 5 and store 6 
print(skipSlice)