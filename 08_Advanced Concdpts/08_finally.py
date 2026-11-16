a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))

try:
    c=a/b
    print(c)
# except Exception as e:
#     print(e)
#this is alwes executed no matter if try completely cxecute or not
finally:
    print("This is alwes executed")