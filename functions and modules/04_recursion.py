'''
0 1 1 2 3 5 8 13
0 1 2 3 4 5 6 7 
fib(0)=0
fib(1)=1
fib(n)=fib(n-1)+fib(n-2)
'''

def fib(n):
    if(n==0 or n==1):
        return n
    return fib(n-1)+fib(n-2)

print(fib(100))