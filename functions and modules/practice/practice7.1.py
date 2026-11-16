# Write a recursive function fibnacci(n) that prints the first n Fibonacci numbers

def fib(k):
    if(k==0 or k==1):
        return k
    return fib(k-1)+fib(k-2)
n=int(input("Enter the number :"))
for i in range(0,n+1):
    print(fib(i),end=" ")