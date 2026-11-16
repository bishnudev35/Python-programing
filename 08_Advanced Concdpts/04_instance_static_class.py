class Employee:
    company='HP'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def print_info(self):
        info= f"the name is {self.name} and the salary is {self.salary}"
        print(info)
    #static method (in static method it would not pass the self)
    @staticmethod
    def sum(a,b):
        return a+b

    #Class Method
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def chage_company(cls,new_company):
        cls.company=new_company
    
e1=Employee("Jack",2354)
e2=Employee("John",2354)
# e1.print_info()
# # print(e2.sum(2,3))TypeError: Employee.sum() takes 2 positional arguments but 3 were given
# # but if we convert the sum method static then it would not give an error
# print(e2.sum(2,3))

e1.print_company()
e1.chage_company("Acer")
e1.print_company()
e2.print_company()