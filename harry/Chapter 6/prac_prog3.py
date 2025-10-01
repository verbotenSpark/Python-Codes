comment = input("enter a comment: ")

# Method 1
if(comment == "Make Mone" or comment =="Click Here" or comment =="Subscribe" or comment =="Buy This"):
    print("Comment is a spam")
else:
    print("Comment Added")

# Method 2
s1 = "Make Mone"
s2 = "Click Here"
s3 = "Subscribe"
s4 = "Buy This"
if(s1 in comment or s2 in comment or s3 in comment or s4 in comment):
    print("Comment is a spam")
else:
    print("Comment Added")
