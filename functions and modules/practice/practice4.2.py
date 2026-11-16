# Write a recursive function sun_of_digits(n)
# that returns the sum of all digits  of a given number

def sum_of_digits(n):
    if(n==0):
       return 0
    digit=n%10
    n=n//10
    sum=digit+sum_of_digits(n)
    return sum


num=int(input("Enter a number :"))
print(sum_of_digits(num))