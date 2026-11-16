# Write a function calcluate_area(length,width=10) that return the are of a rectangle.
# test it by calling the function with 
# 1.both length and width
# 2.only length

def calculate_area(length,width=10):
    return length*width

print(calculate_area(2,5))
print(calculate_area(2))