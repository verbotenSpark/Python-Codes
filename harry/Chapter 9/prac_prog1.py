with open("poems.txt") as f:
    c = f.read()
    word = "mewau"
    if(word in c):
        print(f"{word} found in file")
    else:
        print(f"{word} not found in file")
