def remWrd():
    with open("poems.txt") as f:
        cont = f.read()
    contNew = cont.replace("donke","#####")
    with open("poems.txt","w") as f:
        f.write(contNew)
        
remWrd()