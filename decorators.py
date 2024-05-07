def my_decorator(fun):  
    def wrapper():
        print("This is my first decorator function")
        fun()
        print("Hello it's working")
    return wrapper
    
@my_decorator   
def test():
    print("Hello Subin")
    
test()
    
    