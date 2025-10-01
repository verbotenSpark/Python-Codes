'''
function syntax:

# no input and output
def func1_name():
    var1 = input
    var2 = input

    var3 = var1+var2
    print(var3)

# function with input and output
def func2_name(val1,val2):
    var1 = val1
    var2 = val2

    var3 = var1+var2
    return var3

# in above function the parameters can have a default value in case if a value isnt provided
def func2_name(val1,val2=69):

'''

def sum(a,b):
    c = a + b
    return c

d = sum(2,3)  # function call
print(d)