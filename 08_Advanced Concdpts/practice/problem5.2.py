# Create a custom exception enters a negative number.
# NegativeNumberError and raise it when the user
class NegativeNumberError(Exception):
    pass

n=input("Enter a number : ")
try:
    n=int(n)
    if n<0:
       raise NegativeNumberError("Negative number is not accepted!")
    c=2/n
except ValueError as e:
    print("dont try to bad type cast",e)
except ZeroDivisionError as e:
    print("divide by 0 not possible",e)
except NegativeNumberError as e:
    print(e)
