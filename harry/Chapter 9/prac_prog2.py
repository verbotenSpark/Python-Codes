import random

score = random.randint(1,100)

with open("highScore.txt") as f:
    hs = f.read()
    if(hs == ""):
        hs = 0
    else:
        hs = int(hs)
    print(f"new score: {score}, highScore: {hs}")

if(score > hs):
    with open("highScore.txt","w") as f:
        f.write(str(score))


