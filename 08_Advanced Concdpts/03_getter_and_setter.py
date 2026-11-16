class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @property
    def first_name(self):
        l=self.name.split(" ")
        #print(l)
        return l[0]
    @first_name.setter
    def first_name(self,first):
        l=self.name.split(" ")
        if(len(l)==2):
         new_name=f"{first} {l[1]}"
         self.name=new_name
        else:
           self.name=first

e=Employee("Jack Doe",34353)


# print(e.first_name())
# e.set_first_name("John")
# print(e.first_name())
 
print(e.first_name)
e.first_name="Jhon"
print(e.first_name)