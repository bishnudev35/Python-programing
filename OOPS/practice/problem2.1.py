# Create a class Person with a constructor ( __init__ ) that acceptsname and age
#  as arguments and stores them as instance attributes. 
#  Create an object and print the person’s name and age.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


p=Person("Jack",23)
print(p.name,p.age)