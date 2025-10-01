lineNo = 1
with open("file.txt") as f:
    c = f.readline()
    lineNo += 1
    word = "four"
    while(c != ""):
        c = f.readline()
        if(word in c):
            print(f"{word} is present in file on line {lineNo}")
        lineNo += 1
    else:
        print("word not found")

        
    