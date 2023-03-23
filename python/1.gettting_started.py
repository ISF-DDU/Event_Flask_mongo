# NO header files

"""
    Hello world program
"""
print("Hello world")

# *****************************************************
"""
    Variables
"""

a = 9
print(a)  # prints 'a' to terminal

a = 23          # Integer, also override the variable
b = 99.36       # Float / Double
c = "Hello"     # String
d = 'D'         # character

print(a, b, c, d)

# converting data type one to another
string = "10"
number = int(string)

# *****************************************************
"""
    User input
"""

# taking the username from user.
# by default input() method takes the input value as string.
name = input("Enter username : ")
print(name)