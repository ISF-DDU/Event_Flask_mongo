"""
 Two kind of loops :
    Entry Control -> for and while
    Exit Control  -> do while
"""

# printing one to 10

for i in range(1,10,1):
    print(1)  # indentation is must

# Explaination of range function

for i in "TechTribe":
    print(i)


i=10

# printing 1 to 10 using while.

while i>0 :
    print(i)
    i-=1  # No pre-post decrement like C or C++


# There is no concept of Do-while in python
# but then too we can achive the functionality

end_stat = "tech_tribe"
counter = 0

while True:
    word = input("Enter the secret word: ").lower()
    counter = counter + 1
    if word == end_stat:
        break
    if word != end_stat and counter > 7: 
        break