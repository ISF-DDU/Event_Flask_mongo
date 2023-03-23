class Person:
    # class variable
    count = 0

    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
        Person.count += 1

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def is_adult(age):
        return age >= 18

person1 = Person("John", 25)
person2 = Person("Jane", 30)

print(person1)
print(person2)
print(Person.get_count())
print(Person.is_adult(person1.age))
