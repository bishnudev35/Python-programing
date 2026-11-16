'''day=int(input("Enter a Day number between 1 to 7 :"))
match day:
    case 1:print("the day is Monday")
    case 2:print("the day is Tuesday")
    case 3:print("the day is Wednesday")
    case 4:print("the day is Thruday")
    case 5:print("the day is Friday")
    case 6:print("the day is Saterday")
    case 7:print("the day is Sunday")
    case _:print("Opss you enter a wrong number!")'''
# second question
a=int(input("Enter your first number :"))
b=int(input("Enter your second number :"))
operator=input("Enter an operator +,-,*,/ : ")

match operator:
    case "+":print(a,"+",b,"=",a+b)
    case "-":print(a,"-",b,"=",a-b)
    case "*":print(a,"*",b,"=",a*b)
    case "/":print(a,"/",b,"=",a/b)
    case _: print("Opps sonmething went wrong")