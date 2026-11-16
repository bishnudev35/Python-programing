# Class: Class is a blueprint or a template. Eg. From for and exam that contains
# name, age, electives, father's name etc

# object: Specific instance created from the template(class.). Eg. Form which
# contais the data for John Doe

class Employee:
    company='HP'

    def get_salary(self):
        return 23000


e=Employee()
print(e.get_salary())