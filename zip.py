# name = ["Subin", "Poornima"]
# age = [28, 26]
 
# for person in zip(name, age):
#     print(person)

# import os
# import shutil
# path = 'empty_folder'

# try:
#     # os.remove(path)
#     # os.rmdir(path)
#     shutil.rmtree(path)
# except FileNotFoundError:
#     print("The file not exists")
# except PermissionError:
#     print("Permission Denied")
# except OSError:
#     print("You cannot delete that using that function")
# else:
#     print(path+ "Successfully deleted")
# def division(a, b):
#     try:
#         result = a / b
#         print(result)
#     except:
#         if b == 0:
#             print("You cannot divide a number with zero")
        
# division(10, 0)

# my_list = [1, 2, 3, 4, 5]

# value = my_list[-2]
# print(value)

# import keyword
# print(keyword.kwlist)

# name = input("Enter your name:")
# print("Hello", name + "!") 

# is_valid = True
# is_valid = False
# print(is_valid)

# i = [1, 2, 3, 4, 5]
# # result = sum(i)
# # print(result)

# result = tuple(i)
# print(result)
# i = 0

# while i < 10:
#     print(i)
#     i += 1

# nums = [1, 3, 3, 4, 5, 6]

# it = iter(nums)
# print(it.__next__())
# print(it.__next__())

# print(next(it))

# for i in range(0,5):
#     if i == 2:
#         continue;
#     print(i)

# def division(num):
#     try:
#         result = 10 // num
#         return result
#     except:
#         if num == 0:
#             return "Divison by zero is not possible"
        
# print(division(2))
# from module import square, greet, pi

# square(2)

# greet('Subin')
# print(pi)

# import math

# print(math.pi)

# class Animal:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
        
#     def bark(self):
#         print(f"{self.name} is a {self.breed}")
        
        
        
# dog = Animal('Simba', 'German Shepard')
# manni = Animal('Rambo', 'Dalmatian')
# dog.bark()
# manni.bark()

# person = ['john', 'subin', 'shaheer', 'samuel']

# marks = [ 89, 87, 78, 99]

# for i, j in zip(person, marks):
#     print(f"{i}:{j}")
    
# print(list((zip(person, marks))))

# dic1 = {
#     'a': 1, 
#     'b': 2, 
#     'c': 3 
#     }

# dic2 = {
#     'd': 4,
#     'e': 5,
#     'f': 6
#     }

# result = zip(dic2.keys(), dic1.values())

# for item in result:
#     print(item)