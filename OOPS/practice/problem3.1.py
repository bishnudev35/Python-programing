# Create a base class Animal with a method sound() that prints "some sound"
#  Create a derived class Dog that overrides sound() to print "Break"
#   Create an object of Dog and call sound()

class Animal:
    def sound(self):
        print("Some sound.")

class Dog(Animal):
    def sound(self):
      print("Bark!")


d=Dog()
d.sound()