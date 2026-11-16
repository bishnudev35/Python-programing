numbers=[1,2,3,4,5,6]

def square(x):
    return x*x

new=list(map(square,numbers))
new1=list(map(lambda x:x*x,numbers))
print(new)
print(new1)