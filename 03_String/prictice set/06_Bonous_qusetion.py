# Question 1
# Write a program that counts how many vowels are in a given string
name="hey my name is Bishnudev!"
sum=0
vowels=['a','e','i','o','u']

for char in name.lower():
    if(char in vowels):
        sum+=1

print(sum)

# Qusetion 2
# Take a user input string and check if it is a palindrome (same forwards and backwards).
string=input("Enter a string :")
if(string==string[::-1]):
    print("the string is an palindrome string")
else:
    print("The string is not an palindrome string")