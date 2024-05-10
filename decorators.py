def my_decorator(func):
    
    def wrapper():
        print("Hello ")
        func()
        print("How are you?")
    return wrapper
    

def test():
    print("Subin")
    
x = my_decorator(test)
x()