class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __str__(self):
        info= f"the name is {self.name} and the salary is {self.salary}"
        return info

    def __repr__(self):
        return f"name: {self.name}\nsalary: {self.salary}"
e=Employee("Harry",2354)
print(e.name,e.salary)
# print(e.__str__())
print(str(e))
print(repr(e))