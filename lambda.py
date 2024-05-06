val = lambda x : x ** 2
print(val(2))

add = lambda x, y: x + y
print(add(8, 6)) 

numbers =[1, 2, 3, 4, 5]

new_list = list(map(lambda x: x ** 2, numbers))
print(new_list)