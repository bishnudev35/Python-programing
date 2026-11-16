# Write a function print_details(**kwargs) that prints
# key-value pairs passed as arguments, for example:

def print_details(**kwargs):
    for item in kwargs.keys():
        print(f"{item}: {kwargs[item]}")
 

print_details(name="Alice", age=25, city="Delhi")