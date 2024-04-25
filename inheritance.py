class Animal:
    def __init__(self, name):
        self.name = name
    
    def barks(self):
        print("barks")
        
        
        
class Pet(Animal):
    
    def barks(self):
        super().barks()
        print(f"{self.name}, barks")
        
        
# Dog = Animal("Simba")

# Dog.barks()
obj = Pet("Rambo")

obj.barks()