# empty dictionary is made as : d = {}
# empty set is made as : s = set()

s = {1,3,5,24,63,3,3,3}  # this is a set, no key val pair so no dictionary
print(s)  # sets have non repeting val so 3 will print only once

# set can have multiple datatypes like all other pervious thingies
ns = {169,42.69,True,"wawa",None}
print(ns, type(ns))



# Properties
    # Sets are unordered, even if numbers are inputted in ordered format they may be unordered
    # Sets are unindexed, i.e., elements cant be accessed by index
    # Written items cannot be changed but can be removed
    # sets can't contain repeated values

#methods
ns.add(6969)  # adds given value to the set
print(ns, type(ns))
    # google other methods

# Operations on sets
set = {1,2,34.45, False, "gagaga"}
print(len(set))  # outputs the length of set
set.remove(2)  # removes specified value
print(set)
set.pop()  # pops random value from the set
print(set)
set.clear()  # clears the entire set
print(set)

print("\n")

# unions & intersections
s1 = {0,1,3,5,7,9}
s2 = {0,2,4,6,8,9}

print(s1.union(s2))  # combines both sets
print(s2.intersection(s1))  # only prints common elements of both sets
