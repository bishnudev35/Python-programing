# Use the walrus operator to read input until the user enters "quit".
# print each input as it is entered.

while(data:=input("Enter your thought....: ")):
    if(data=="quit"):
        break
    print(data)