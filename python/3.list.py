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

# now, we want to update element at index 1
l[1] = 99.36
print(l)

# merging two lists into new list z
x = [1, 2, 3]
y = [9, 8, 7]
z = x + y
print(z)


# Important to deal with MongoDB
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

# appending one dict to another
d1 = {
    "name": "tomy",
    "email": "tomy@gmail.com"
}
d2 = {
    "contact": 7984564562
}
print(d1)
print(d2)

# method 1
d1.update(d2)
print(d1)

# method 2
d3 = {**d1, **d2}
print(d3)