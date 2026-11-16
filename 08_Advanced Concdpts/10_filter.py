def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False

a=[23,53,756,2,4,67,324,2,4,5,7,99]
new=list(filter(is_greater_than_9,a))
new1=list(filter(lambda x:x>9,a))
print(new)
print(new1)