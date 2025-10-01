a = "hello  world"
nt = a.count("  ")
print(nt)
if (nt == 1) :
    print("double space detected")
    a = a.replace("  "," ")
print(a)

emali = "dear gaga,\n googoo gaga. \nthanks"
print(emali)