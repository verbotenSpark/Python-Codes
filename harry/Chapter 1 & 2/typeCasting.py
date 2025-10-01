# Type Determination

# integer type
a = 9
typ = type(a)      #type(_) tells about the type of the variable it has been given
print(typ)

# float type
a = 6.9
typ = type(a)
print(typ)

# string type
a = "meoooow"
typ = type(a)
print(typ)




print("\n")



# typeCast

a = "42.69"
print(type(a))    # a is of string type
a = float(a)   # typecasting a to float
print(type(a))

# similar functions:
# str(a)   but a should be valid to be converted to a string
# int(a)
