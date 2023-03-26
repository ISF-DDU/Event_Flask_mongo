class Person:
    # class variable
    count = 0

    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
        Person.count += 1

    def toString(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def is_adult(self):
        return self.age>=18


person1 = Person("John", 25)
person2 = Person("Jane", 30)

print(person1.age)
print(person2.toString())
print(Person.count)
print(person2.is_adult())