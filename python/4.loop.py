"""
 Two kind of loops :
    Entry Control -> for and while
    Exit Control  -> do while
"""

# printing 1 to 10
for i in range(1, 11):   # for(int i=1;i<11;i++)
    print(i)           # indentation is must

# printing 0, 2, 4,...10.
for i in range(0, 11, 2): #for (int i=0;i<11;i+=2)
    print(i)

# appending the 1 to 10 numbers in list.
numbers = []   # numbers=list()
for i in range(11):
    numbers.append(i)
print(numbers)


# printing 1 to 10 using while.
i=10

while i>0 :
    print(i)
    i-=1         # No pre-post decrement like C or C++
    # i++, --i i-=1-> i= i-1


# There is no concept of Do-while in python
# but then too we can achive the functionality

end_stat = "tech_tribe"
counter = 0

while True:
    word = input("Enter the secret word: ").lower() # .upper()
    counter = counter + 1
    if word == end_stat:
        break
    if word != end_stat and counter > 7: 
        break