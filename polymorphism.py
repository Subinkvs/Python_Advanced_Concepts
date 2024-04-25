# class French:
    
#     def say_hello(self):
#         print('Hello in French')
        
        
# class Spanish:
    
#     def say_hello(self):
#         print('Hello in Spanish')
        
        


# def greet(Lang):
#     Lang.say_hello()
    
    

# Subin = French()
# john = Spanish()

# greet(Subin)
# greet(john)
    
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def barks(self):
#         print(f"{self.name} barks")

# class Dog(Animal):
#     def barks(self):
#         super().barks()
#         print(f"{self.name} barks louder")

# def speak(name):
#     pet = Animal(name)
#     pet1 = Dog(name)
    
#     pet.barks()
#     pet1.barks()

# speak('Rambo')
# speak('Simba')

# class Animal:
    
#     def barks(self):
#         print("Some Animals barks")
        
        
# class Dog(Animal):
#     # method overriding
#     def barks(self):
#         super().barks()
#         print("Dogs barks")
        
        
# obj = Dog()

# # obj.barks()

# class Operations:
    
#     def add(self, a, b):
#         return a + b
    
#     def add(self, a, b, c):
#         return a + b + c
    
    
# obj = Operations()
# print(obj.add(1, 2))
# print(obj.add(1, 2, 4))