# Use reduce() from functools to find the product of all elements in [1,2,3,4]
from functools import reduce
num=[1,2,3,4]
product=reduce(lambda x,y:x*y,num)
print(product)