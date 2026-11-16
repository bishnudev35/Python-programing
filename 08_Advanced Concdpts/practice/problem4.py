# Create a class Book with attributes title and author .
# 1.Implement __str__() so that printing the object displays "Title by Author" .
# 2.Implement __len__() so that len(book) returns the length of the title.

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def __str__(self):
       return f"{self.title} by {self.author}"

    def __len__(self):
        return len(self.title)


b=Book("Gitanjali","R.N Tagor")
print(str(b))
print(len(b))
 #Question 2: Create two Book objects and test these methods.
b1=Book("Aparajit","Satyajit Ray")
b2=Book("Chander Pahar","Bibhutibhusan Bandhopadhya")

print(str(b1),len(b1))
print(str(b2),len(b2))
