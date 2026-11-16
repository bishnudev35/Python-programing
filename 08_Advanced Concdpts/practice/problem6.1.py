# Use map() to convert [1, 2, 3, 4, 5] into their cubes.

number=[1, 2, 3, 4, 5]

result=list(map(lambda x:x**3,number))
print(result)