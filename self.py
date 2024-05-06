class MyClass():
    
    cls = 10
    
    def __init__(self, x):
        self.x = x
        
    def set_x(self, x):
        self.x = x
     
    @staticmethod   
    def static_method():
        print("This is a static method")
        
    @classmethod  
    def class_method(x):
        print(x.cls)
        
        
        
        
obj1 = MyClass(5)
print(obj1.x)
obj1.set_x(10)
print(obj1.x)
MyClass.static_method()
MyClass.class_method()