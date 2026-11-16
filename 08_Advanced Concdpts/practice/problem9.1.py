# Combine a decorator with *args and  **kwargs support so it can wrap any
# function regardless of its parameters.

from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Positional arguments (args): {args}")
        print(f"Keyword arguments (kwargs): {kwargs}")

        # Call the original function with all its arguments and return its result
        return func(*args, **kwargs)

    return wrapper


# Test 1: Function with positional arguments
@decorator
def add(a, b):
    return a + b


# Test 2: Function with keyword and default arguments
@decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print("Result 1:", add(5, 3))
print("-" * 30)
print("Result 2:", greet("Alice", greeting="Welcome"))
