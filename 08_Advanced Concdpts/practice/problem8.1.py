# Write a function sum_all(*args)
# that accepts any number of integers and returns their sum.

def sum_all(*args):
    total=0
    for item in args:
        total+=item
    return total


print(sum_all(2,3,4,5,6))