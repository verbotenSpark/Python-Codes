def remWrd():
    li = ["donke","maw","miyao","meaw"]
    with open("poems.txt") as f:
        cont = f.read()
        contNew = cont
    for i in range(0,len(li)):
        contNew = contNew.replace(str(li[i]),"#"*len(li[i]))
    with open("poems.txt","w") as f:
        f.write(contNew)
        
remWrd()