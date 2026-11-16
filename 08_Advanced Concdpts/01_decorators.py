# Decorator is a function that takes a function, it create a new function
# inside the body (wrapper). the it returns that new fucntion


def decorator(fun):
    def wrapper():
        print("I am about to execute a function....")
        fun()
        print("I hve executed this function...")

    return wrapper

def say_hello():
     print("Hello!")

# say_hello()
f=decorator(say_hello)

'''
f will look like something this
def f():
   print("I am about to execute a function....")
   print("Hello!")
   print("I hve executed this function...")
  
'''
f()

# in the  other way we can do the same

def decorator(fun):
    def wrapper():
        print("I am about to execute a function....")
        fun()
        print("I hve executed this function...")

    return wrapper
@decorator
def say_hello():
     print("Hello!")

say_hello()

