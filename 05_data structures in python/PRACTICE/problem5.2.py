# Create a dictionary of three friends and their phone numbers. Use:
# 1.keys() to get all names
# 2.values() to get all numbers
# 3.items() to loop over key-value pairs and print them

phone_no={}
for i in range(3):
    name=input("Enter the name of friends :")
    no=input("Enter the phone no of {name} :")
    phone_no[name]=no

print(phone_no.keys())
print(phone_no.values())
print(phone_no.items())

