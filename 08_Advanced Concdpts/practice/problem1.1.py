# Write a decorator logger that prints "Function is being called" before the function runs.
# Use it to decorate a function say_hello() taht prints "Hello!"

def decorator(func):
    def wraper():
        print("Function is being called")
        func()
    return wraper
@decorator
def say_hello():
    print("Hello!")

say_hello()
