# def very_slow_func():
#     print("Prining something.....")
#     print("Prining something.....")
#     print("Prining something.....")
#     print("Prining something.....")
#     print("Prining something.....")
#     print("Prining something.....")
#     print("Prining something.....")
#     return 70

# a=very_slow_func()
# if(a>10):
#     print(a)

# else:
#     print("Its not greater than 10")

# #using walrus function we can write same thing
# if((a:=very_slow_func())>10):
#     print(a)
# else:
#     print("it not greater than 10")


while(data:=input("Enter the vaule: ")):
    if(data=='q'):
        break
    print(data)