# Dictionary is a collection of key: value pairs 
# its like a list but value can be obtained by inputting required key

dicktionary = {
    "key":"value",
    "stud1": 100,
    "fruit":"banyana",
    "plane":737,
    42.69 :"hehe"
}

print(dicktionary["fruit"])
print(dicktionary[42.69])

# Properties:  1.unordered  2.Mutable  3.Indexed  4.Duplicate keys not allowed

# Methods

print(dicktionary.items())   # returns a (key,value) tuple pair
print(dicktionary.keys())    # returns keys present in it
print(dicktionary.values())  # same as keys but for values
dicktionary.update({"stud1": 69})  # updates value for given key & can add new key,value pairs too
print(dicktionary)
print(dicktionary.get("plane")) # retrives value for given key
