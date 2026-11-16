# create a list [1,2,3,4,5] and use map() with a lambda function to get their sqares


square=lambda x:x*x
list1=[1,2,3,4,5] 

print(list(map(square,list1)))