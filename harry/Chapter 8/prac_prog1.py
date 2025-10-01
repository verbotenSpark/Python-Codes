def gr8est(n1,n2,n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2 >n3):
        return n2
    else:
        return n3

def intInp():
    no = int(input(""))
    return no

print("enter 3 numbers:")
n1 = intInp()
n2 = intInp()
n3 = intInp()
gr8 = gr8est(n1,n2,n3)
print(gr8)
