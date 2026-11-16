class Employee:
    def __init__(self,name,salary,bond):
        self.name=name
        self.salary=salary
        self.bond=bond

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the Employee is {self.name}.Salary is {self.salary}. The Bond is for {self.bond} years")


e1=Employee("John Doe",42000,2)
e1.get_info()