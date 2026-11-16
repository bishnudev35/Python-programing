# question 1
#  Print numbers from 1 to 10 using a while loop
'''a=1
while a<=10:
    print(a)
    a+=1'''

# question 2
# Write a program that keeps asking the user to enter a password until they
'''password=1234
while True:
    x=int(input("Enter the password :"))
    if x==password:
        print("sucessfully logdin!")
        break
    else:print("please enter the correct password :")'''
# question 3
# Use a while loop to reverse a given number (e.g., 123 → 321).
number=int(input("Enter a number :"))
print("so the reverse number is :")
while number!=0:
      digit=number%10
      number=number//10
      print(digit,end='')
