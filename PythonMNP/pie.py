"""
import math

pie = math.pi
lis = []
lisnum = []
lisden = []
numMax = 500
for num in range(300,numMax):
    for den in range(100,(int)(numMax/3)):
        if abs(num/den) > 3.141592:
            lis.append(abs(pie-(num/den)))
            lisnum.append(num)
            lisden.append(den)

for i in range(len(lis)):
    if lis[i] == min(lis):
        # print(f"{lisnum[i]}/{lisden[i]} = {lis[i]} = {pie+lis[i]}, pi = {pie}")
        print(f"calculated result = {lisnum}/{lisden} = {pie+lis[i]}, pi = {pie}")

        """