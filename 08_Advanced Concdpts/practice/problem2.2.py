# Create an object and test by setting positive and negative salaries.

class Employee:
    def __init__(self,_salary):
        self.salary=_salary
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,new_salary):
        if new_salary<0:
            raise Warning("Salary can't be negative!")
        else :
            self._salary=new_salary


e=Employee(3254)
e2=Employee(-435)