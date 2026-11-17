while(x:=input(("Enter the first number(or 'q' to quit): "))):
    try:
        if x=='q' or x=='quit':
            break
        a=int(x)
        b=int(input("Enter the second number :"))
        print("What kind of operation do you want to perform:\npress + for addition.\npress - for substruction\npress / for division.\npress * for multiplication")
        o=input("Enter the Operation: ")

        match o:
            case '+':
                print(f"The result is: {a+b}")
            case '-':
                print(f"The result is: {a-b}")
            case '/':
                print(f"The result is: {a/b}")
            case '*':
                print(f"The result is: {a*b}")
            case default:
                print("The Operation is not a valid operation!")
    except ZeroDivisionError:
        print("Error: You cant divide by Zero")
    except Exception as e:
        print("Enter a valid value of a and b")