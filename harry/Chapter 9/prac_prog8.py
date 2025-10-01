with open("poems.txt") as f:
    c = f.read()

with open("poems_copy.txt","w") as f:
    f.write(c)

with open("poems_copy.txt") as f:
    cc = f.read()

if(c == cc):
    print("Same content")

with open("poems_copy.txt","w") as f:
    f.write("")