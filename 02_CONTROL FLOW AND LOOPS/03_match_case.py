num=int(input("Enter a number bewteen 1 to 10 :"))

match num:
    case 1:
        print("you wown a charger")
    case 6:
        print("you wown a $3 cuppon card")
    case 8:
        print("You wown a camera")
    case _:
        print("Better Luck next time!")
# it like switch case in other language
