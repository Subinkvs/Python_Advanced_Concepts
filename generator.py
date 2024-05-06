def generator_fun():
    yield 1
    yield 2
    yield 3
    
obj = generator_fun()

for i in obj:
    print(i)