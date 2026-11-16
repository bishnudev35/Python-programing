# Write a decorator  timer that calculates how long a function takes to execute. 
# Test it with a function that sums numbers from 1 to 1,000,000
from functools import wraps
import time
def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time=time.perf_counter()
        response=func(*args,**kwargs)
        end_tiem=time.perf_counter()

        taken_time=end_tiem-start_time
        print(f"Function '{func.__name__}' executed in {taken_time:.6f} second")
        return response
    return wrapper

@timer
def sum_numbers(limit):
    sum=0
    for i in range(limit):
        sum+=i
    return sum


total=sum_numbers(1000000)
print(f"Result: {total}")

        