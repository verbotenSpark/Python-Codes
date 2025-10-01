def cTf(c):
    f = (c * 9/5) + 32
    return f

c = int(input("ENter *c: "))
print(f"{c}*C = {cTf(c)}*F")

print("NO new line after this print statement",end="")