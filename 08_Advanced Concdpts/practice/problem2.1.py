# Create a class Employee with a private attribute _salary .
# 1.Use @property to define a getter for salary .
# 2.Use @salary.setter to prevent setting negative values (print a warning instead).

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


e=Employee(-124)
print(e.salary)
e.salary=666666
print(e.salary)
       
# class Employee:
#     def __init__(self, salary):
#         # Assign to self.salary (not self._salary) so the setter validates the initial value too
#         self.salary = salary

#     @property
#     def salary(self):
#         return self._salary

#     @salary.setter
#     def salary(self, new_salary):
#         if new_salary < 0:
#             print("Warning: Salary can't be negative!")
#         else:
#             self._salary = new_salary


# # Test the class
# e = Employee(-3500)
# print(e.salary)  # Output: 3500

# e.salary = -500  # Output: Warning: Salary can't be negative!
# print(e.salary)  # Output: 3500 (remains unchanged)

# e.salary = 666666
# print(e.salary)  # Output: 666666
