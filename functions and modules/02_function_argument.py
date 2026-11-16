# def add(a,b):
#     return a+b

# c=add(2,4)
# print(c)

# default aregument
def add(a,b,plaus=0):
    c=a+b+plaus
    return c

ans=add(2,3)
ans1=add(2,4,6)
print(ans)
print(ans1)
# Keyword argument
ans2=add(b=2,a=2)
print(ans2)