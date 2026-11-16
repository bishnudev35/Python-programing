class Employee:
    company="HP" # this is class attribute
    def __init__(self,name,salary,bond,company=company):
        self.name=name # create an instance attribute 
        self.salary=salary
        self.bond=bond
        self.company=company

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the Employee is {self.name}.Salary is {self.salary}. The Bond is for {self.bond} years")


e1=Employee("John Doe",42000,2)
e2=Employee("Jack",23400,1,"Asush")
print(e1.company,e2.company)

print(dir(e1))