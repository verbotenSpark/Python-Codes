with open("file.txt") as f:
    c = f.read()
    word = "four"
    if(word in c):
        print(f"{word} is present in file")