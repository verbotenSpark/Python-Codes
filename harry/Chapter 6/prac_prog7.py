post = "baby shark dodododo mommy sakh dododod dady shark dododo"
name = "sakh"

# Method 1
if(post.__contains__(name)== True):
    print(f"{name} is present in song")
else:
    print(f"{name} is not present in song")

# Method 2
if(name.lower() in post.lower()):
    print(f"{name} is present in song")
else:
    print(f"{name} is not present in song")