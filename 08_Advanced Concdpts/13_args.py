def sum(*args):
    #args will be a tuple of all the values passed to sum
    total=0
    for item in args:
        total+=item
    return total

print(sum(12,43,5,3,6))