#we know that strings are immutable and performing operations produces a new string
#whereas lists are mutable so producing new lists is not required although the program produces a list but we don't use it


thingies = ["human","animala",5,67.98,True,"maww"]   #list can store multiple datatypes

print(thingies[1])            #print data at index 1
thingies[1] = "birdie"        #modify data at index 1
print(thingies[1])

# print(type(thingies[3]))    #print type of data at index 3

thingies.append("kawkaw")     #add kawkaw at the end
print(thingies)               #print list

noList = [34,23,56,14,72,12,19]
noList.sort()
print(noList)
noList.reverse()
print(noList)
noList.insert(0,99)
print(noList)
noList.pop(3)
print(noList)

