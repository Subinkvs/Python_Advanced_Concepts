# def generator_func(n):
#    while n <= 5:
#        yield n
#        n += 1
    
# x = generator_func(1)

# for i in x:
#     print(i)

def outer():
    x = 5
    
    def inner():
        nonlocal x 
        x = 10
        print(x)
        
    inner()
    print(x)
    
outer()