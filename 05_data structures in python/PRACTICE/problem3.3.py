# Convert the tuple to a list, change its first element to 50 ,
#  and convert it back to a tuple.
tu=(1,2,3,4)
print(tu)
list=list(tu)
list[0]=50
tu=tuple(list)
print(tu)