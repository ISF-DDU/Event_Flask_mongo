# Lists

# list declaration
a = list()
b = []

# 'append()' method to add elements in list
# let say we want to add "Apple" in list a.

a.append("Apple")
print(a)

# we can add different types of data type elements in same list
l = [1, 'A', 5.5, "Tech Tribe"]
print(l)
print(i for i in l)

# now, we want to update element at index 1
l[1] = 99.36
print(l)

# merging two lists into new list c
c = a + l
print(c)


# Important to deal wiht MongoDB
# Same format as JSon -> Javascript object notation



# Dictionary

# Declaring the empty dict by two ways
dict1 = dict()
dict2 = {}

a = [1, 2, 3, 4, 5]
dict = {
    "Name": "Minato",
    "Nick-name": "Yellow Flash",
    "post": "Hokage",
    "Missons": 999,
    "stars": a
}
print(dict)

# Creting the element of dictionary
dict2["stars"] = a
print(dict2)