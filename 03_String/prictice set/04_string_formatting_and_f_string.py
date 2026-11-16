#Qusetion 1
#  Using format() , create a sentence:
# "My name is John and I am 25 years old."
# by passing "John" and 25 as variables.
template="My name is {} and I am {} years old."
name="John"
age=25
print(template.format(name,age))

# Question 2
# Do the same using f-strings
print(f"My name is {name} and I am {age} years old.")
