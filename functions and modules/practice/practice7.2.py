# Write a function safe_divide(a,b) that returns the result of a/b,
# but returns "Cant divide by Zero" if b is 0

def safe_divide(a,b):
    if b==0:
        return "Cant divide by Zero!"
    return a/b

print(safe_divide(3,2))
print(safe_divide(2,0))