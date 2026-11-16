# Write a recursive function factorial(n) taht returns the factorial of a number

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

print(factorial(3))