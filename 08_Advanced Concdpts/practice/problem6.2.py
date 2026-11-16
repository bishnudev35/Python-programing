# Use filter() to get only even numbers from  [10, 11, 12, 13, 14] .

number=[10, 11, 12, 13, 14]
def even(x):
    if x%2==0:
        return True
    else:
        return False
res=list(filter(even,number))
print(res)