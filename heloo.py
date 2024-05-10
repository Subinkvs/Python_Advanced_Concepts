def my_decorator(diff):
    def wrapper(a,b):
        y = diff(a,b)
        return abs(y) 
    return wrapper
            

@my_decorator
def diff(a,b):
    return a - b

print(diff(2, 5))