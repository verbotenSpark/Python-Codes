def mult(n,i=1):
    if(i == 11):
        return
    print(i*n)
    mult(n,i+1)

mult(6)