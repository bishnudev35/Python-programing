# def sum(a,b):
#     print("Hey i am summing.......")
#     c=a+b
#     z=0#here z behabe like local variable
#     return c

# z=5
# print(sum(2,13))
# print(z)



def sum(a,b):
    print("Hey i am summing.......")
    c=a+b
    global z # this provide access to the global variable
    z=0#now z behalf like global variable
    return c

z=5
print(sum(2,13))
print(z)