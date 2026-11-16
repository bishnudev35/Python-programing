class Animal: #parent class (super Class)
    location="Australia"
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Speaking now....")

class Dog(Animal):#this is how inheritance iw done in python
    def speak(self):
        super().speak() # we are using the speak function of the parent class
        print("Woof!")


d=Dog("Bruno")
d.speak()
print(d.location)