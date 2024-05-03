# dic1 = {
#     "name": "Subin",
#     "age": 28
# }

# dic2 = {
#      "name": "nimi",
#      "age": 10
# }

# dic7 = {
#      "name": "nima",
#      "age": 10
# }

# dic8 = {
#      "name": "nami",
#      "age": 10
# }

# dic3 = {
#     "name": "Sanju",
#     "age": 29
# }

# dic4 = {
#     "name":"Suhail",
#     "age": 24

# }

# dic5 = {
#     "name":"Sonu",
#     "age": 24

# }

# dic6 = {
#     "name":"Sworav",
#     "age": 24

# }

# list = [dic1, dic2, dic3, dic4, dic5, dic6, dic7, dic8]



# def SearchName(list, char):
    
#     count = 0
    
#     for item in list:           
#         if item['name'][0] == char:
#             count = count + 1
#             if count < 3:
#                 print(item)
            
        

        
# SearchName(list, 'n')

# def test_tuple():
    
#     list = [11, 22, 33, 44, 55, 66, 220]
#     for i in list:
#         print(i)
    
#     tuple = (1, 2, 3, 4, 5, 6)
#     for i in tuple:
#         print(i)
        
# test_tuple()
# import sys

# list = [1, 2, 3, 4, 5]
# tuple = (1, 2, 3, 4, 5)

# print(sys.getsizeof(list))
# print(sys.getsizeof(tuple))


# tuple = ('Subin', 28, 'Software Engineer')

# name, age, profession = tuple

# print("Name:", name, "Age:", age, "Profession:", profession)

# name, *rest = tuple

# print(rest)


# first, *second = list

# print(second)

# name = dic1["name"]
# print(name)


# x = 4
# x = 5 

# y = x + x
# print(y)

# x = 4
# y = 6

# print(x + y)

# data = [(1, 'one'), (2, 'two'), (3, 'three')]

# for digit, _ in data:
#     print(digit)

data = [
    {"name":"Subin","age": 28},
    {"name":"Jonh","age": 10},
    {"name":"kyle","age" : 28},
    {"name": "telusko","age": 38}
]

data.sort(key = lambda person: person['age'])

print(data)

def call(func): 
    func()
    
def add(x, y):
    print(x + y)

call(lambda: add(2, 3))


