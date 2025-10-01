def genTables(no):
    table = ""
    for i in range(1,11):
        table += f"{no} * {i} = {no*i}\n"
    with open(f"Chapter 9/Tables/table-{no}.txt","w") as f:
        f.write(table)
    
for i in range(2,21):
    genTables(i)